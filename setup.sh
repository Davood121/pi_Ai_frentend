#!/bin/bash

echo "🧠 Setting up AI Brain Pi Frontend..."

# Update system
sudo apt update

# Install Python pip if not installed
sudo apt install -y python3-pip

# Install Python dependencies
pip3 install -r requirements.txt

# Make scripts executable
chmod +x terminal_chat.py

echo "✅ Setup complete!"
echo ""
echo "🚀 Quick Start:"
echo "1. Update your laptop IP in config.py"
echo "2. Run web interface: python3 app.py"
echo "3. Run terminal chat: python3 terminal_chat.py"
echo ""
echo "🌐 Web interface will be available at: http://your-pi-ip:5000"