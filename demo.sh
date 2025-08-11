#!/bin/bash
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
