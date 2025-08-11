#!/usr/bin/env python3
"""
ShadowPrint Demonstration Setup
This script creates sample files and demonstrates ShadowPrint usage safely
"""

import os
import subprocess
import time

def create_sample_executable():
    """Create a harmless sample executable-like file for demonstration"""
    print("🔧 Creating sample executable file...")
    
    # Create a simple Python script that looks like an executable
    sample_code = '''#!/usr/bin/env python3
"""
Sample Application - Windows Update Utility
This is a demonstration file for ShadowPrint
"""
import sys
import time

def main():
    print("=" * 50)
    print("Windows Update Utility v2.1.0")
    print("Microsoft Corporation")
    print("=" * 50)
    print("Checking for updates...")
    
    for i in range(3):
        print(f"Progress: {i+1}/3")
        time.sleep(0.5)
    
    print("No updates available.")
    print("System is up to date!")
    print("=" * 50)

if __name__ == "__main__":
    main()
'''
    
    with open("sample_app.py", "w") as f:
        f.write(sample_code)
    
    # Make it executable
    os.chmod("sample_app.py", 0o755)
    print("✅ Created sample_app.py")

def create_demo_script():
    """Create a demonstration script that shows ShadowPrint usage"""
    print("📝 Creating demonstration script...")
    
    demo_script = '''#!/bin/bash
# ShadowPrint Demonstration Script
# This script demonstrates how ShadowPrint works

echo "🔍 ShadowPrint Demonstration"
echo "================================"
echo ""

echo "📋 Step 1: Show the original file"
echo "File: sample_app.py"
echo "Size: $(ls -lh sample_app.py | awk '{print $5}')"
echo "Permissions: $(ls -la sample_app.py | awk '{print $1}')"
echo ""

echo "📋 Step 2: Demonstrate certificate cloning from google.com"
echo "Running: python3 ShadowPrint_v2.py --host google.com sample_app.py signed_sample_app.exe"
echo ""

# Run ShadowPrint with google.com
python3 ShadowPrint_v2.py --host google.com sample_app.py signed_sample_app.exe

echo ""
echo "📋 Step 3: Show the signed file"
if [ -f "signed_sample_app.exe" ]; then
    echo "✅ Successfully created signed_sample_app.exe"
    echo "Size: $(ls -lh signed_sample_app.exe | awk '{print $5}')"
    echo ""
    echo "📋 Step 4: Show certificate information"
    if [ -d "certs" ]; then
        echo "Generated certificates:"
        ls -la certs/
        echo ""
        echo "Certificate details:"
        openssl x509 -in certs/google.com.crt -text -noout | head -20
    fi
else
    echo "❌ Failed to create signed file"
fi

echo ""
echo "🎯 Demonstration Complete!"
echo "This shows how ShadowPrint can clone certificates and sign executables"
echo "for AV evasion purposes."
'''
    
    with open("demo.sh", "w") as f:
        f.write(demo_script)
    
    os.chmod("demo.sh", 0o755)
    print("✅ Created demo.sh")

def create_safety_notice():
    """Create a safety notice file"""
    print("⚠️  Creating safety notice...")
    
    safety_text = """⚠️  SHADOWPRINT SAFETY NOTICE ⚠️

This tool is designed for AV (Antivirus) Evasion and should ONLY be used for:

✅ LEGITIMATE PURPOSES:
- Security research and testing
- Authorized penetration testing
- Educational demonstrations
- Testing your own systems
- Certificate security research

❌ NEVER USE FOR:
- Bypassing security on systems you don't own
- Malicious activities
- Unauthorized testing
- Harmful purposes

🔒 RESPONSIBLE USAGE:
- Always obtain proper authorization
- Use only on systems you control
- Follow ethical hacking guidelines
- Respect privacy and security

📚 EDUCATIONAL VALUE:
This demonstration shows how:
1. SSL certificates can be cloned from legitimate websites
2. Executables can be digitally signed with spoofed certificates
3. Antivirus software can potentially be bypassed
4. Certificate security can be compromised

Remember: With great power comes great responsibility!
"""
    
    with open("SAFETY_NOTICE.txt", "w") as f:
        f.write(safety_text)
    
    print("✅ Created SAFETY_NOTICE.txt")

def main():
    """Main demonstration setup"""
    print("🚀 Setting up ShadowPrint Demonstration")
    print("=" * 50)
    
    # Create sample files
    create_sample_executable()
    create_demo_script()
    create_safety_notice()
    
    print("\n🎉 Setup Complete!")
    print("\n📋 Files created:")
    print("  - sample_app.py (sample executable)")
    print("  - demo.sh (demonstration script)")
    print("  - SAFETY_NOTICE.txt (safety guidelines)")
    print("\n🚀 To run the demonstration:")
    print("  ./demo.sh")
    print("\n⚠️  Remember: This tool is for educational purposes only!")
    print("   Always use responsibly and ethically.")

if __name__ == "__main__":
    main() 