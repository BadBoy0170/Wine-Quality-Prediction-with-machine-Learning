#!/usr/bin/env python3
"""
Simplified ShadowPrint Demonstration
Focuses on certificate cloning capabilities
"""

import ssl
from OpenSSL import crypto
from pathlib import Path
import sys

def clone_certificate(host, port=443):
    """Clone SSL certificate from a host"""
    print(f"🔍 Cloning certificate from {host}:{port}")
    
    try:
        # Fetch the certificate
        print(f"[+] Fetching certificate from {host}:{port}")
        cert_data = ssl.get_server_certificate((host, port))
        
        # Parse the certificate
        x509 = crypto.load_certificate(crypto.FILETYPE_PEM, cert_data.encode())
        
        print(f"✅ Successfully downloaded certificate from {host}")
        print(f"   Subject: {x509.get_subject()}")
        print(f"   Issuer: {x509.get_issuer()}")
        print(f"   Valid from: {x509.get_notBefore()}")
        print(f"   Valid until: {x509.get_notAfter()}")
        print(f"   Key size: {x509.get_pubkey().bits()} bits")
        
        # Create directory for certificates
        cert_dir = Path('demo_certs')
        cert_dir.mkdir(exist_ok=True)
        
        # Generate new key with minimum size
        print(f"\n🔑 Generating new RSA key...")
        key_bits = max(x509.get_pubkey().bits(), 2048)
        new_key = crypto.PKey()
        new_key.generate_key(crypto.TYPE_RSA, key_bits)
        print(f"   Generated {key_bits}-bit RSA key")
        
        # Create cloned certificate
        print(f"\n📜 Creating cloned certificate...")
        cloned_cert = crypto.X509()
        cloned_cert.set_version(x509.get_version())
        cloned_cert.set_serial_number(x509.get_serial_number())
        cloned_cert.set_subject(x509.get_subject())
        cloned_cert.set_issuer(x509.get_issuer())
        cloned_cert.set_notBefore(x509.get_notBefore())
        cloned_cert.set_notAfter(x509.get_notAfter())
        cloned_cert.set_pubkey(new_key)
        cloned_cert.sign(new_key, 'sha256')
        
        # Save files
        cert_file = cert_dir / f"{host}.crt"
        key_file = cert_dir / f"{host}.key"
        
        with open(cert_file, 'wb') as f:
            f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cloned_cert))
        
        with open(key_file, 'wb') as f:
            f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, new_key))
        
        print(f"✅ Certificate files created:")
        print(f"   Certificate: {cert_file}")
        print(f"   Private Key: {key_file}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("""🔐 ShadowPrint Certificate Cloning Demo
============================================

This demonstration shows how ShadowPrint can clone SSL certificates
from legitimate websites for educational purposes.

⚠️  WARNING: This tool is for educational use only!
    Never use for malicious purposes.
""")
    
    # Test with multiple websites
    websites = [
        ("google.com", 443),
        ("github.com", 443),
        ("microsoft.com", 443)
    ]
    
    for host, port in websites:
        print(f"\n{'='*60}")
        if clone_certificate(host, port):
            print(f"🎯 Successfully cloned {host} certificate!")
        else:
            print(f"💥 Failed to clone {host} certificate")
        print(f"{'='*60}")
    
    print(f"\n🎉 Demonstration Complete!")
    print(f"📁 Check the 'demo_certs' directory for generated files")
    print(f"🔒 Remember: These certificates are for educational purposes only!")

if __name__ == "__main__":
    main() 