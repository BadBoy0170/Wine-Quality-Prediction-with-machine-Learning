#!/bin/bash
# ShadowPrint Quick Start Script
# This script sets up and runs the ShadowPrint demonstration

echo "🚀 ShadowPrint Quick Start"
echo "=========================="
echo ""

# Check if we're in the right directory
if [ ! -f "ShadowPrint_v2.py" ]; then
    echo "❌ Error: Please run this script from the ShadowPrint directory"
    exit 1
fi

# Check Python version
echo "🔍 Checking Python version..."
python3 --version
if [ $? -ne 0 ]; then
    echo "❌ Error: Python3 is not installed"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "shadowprint_demo" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv shadowprint_demo
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source shadowprint_demo/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install pyopenssl

# Check osslsigncode
echo "🔍 Checking osslsigncode..."
if ! command -v osslsigncode &> /dev/null; then
    echo "⚠️  osslsigncode not found. Installing..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install osslsigncode
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt-get update
        sudo apt-get install -y osslsigncode
    else
        echo "❌ Unsupported OS. Please install osslsigncode manually."
        exit 1
    fi
fi

echo "✅ Dependencies installed successfully!"
echo ""

# Run the setup script
echo "🔧 Setting up demonstration files..."
python3 demo_setup.py

echo ""
echo "🎯 Ready to demonstrate ShadowPrint!"
echo ""
echo "📋 Available demonstration methods:"
echo "1. Full tool demonstration:"
echo "   python3 ShadowPrint_v2.py --host google.com sample_app.py signed.exe"
echo ""
echo "2. Simplified certificate cloning:"
echo "   python3 simple_demo.py"
echo ""
echo "3. Automated demo script:"
echo "   ./demo.sh"
echo ""
echo "📚 Documentation:"
echo "   - COMPLETE_DEMO_GUIDE.md (comprehensive guide)"
echo "   - DEMONSTRATION_GUIDE.md (recording script)"
echo "   - SAFETY_NOTICE.txt (safety guidelines)"
echo ""
echo "⚠️  Remember: This tool is for educational purposes only!"
echo "   Always use responsibly and ethically."
echo ""
echo "🎬 Happy demonstrating!" 