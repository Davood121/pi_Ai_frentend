# 🧠 AI Brain Pi Frontend

Raspberry Pi frontend interface for the AI Brain System. Connect your Pi to your laptop's AI Brain and start chatting!

## 🚀 Quick Setup

### 1. Download to Raspberry Pi
```bash
git clone https://github.com/yourusername/AI_Brain_Pi_Frontend.git
cd AI_Brain_Pi_Frontend
```

### 2. Run Setup
```bash
chmod +x setup.sh
./setup.sh
```

### 3. Configure Your Laptop IP
Edit `config.py` and update your laptop's IP address:
```python
LAPTOP_IP = "YOUR_LAPTOP_IP_HERE"
```

## 🖥️ Interface Options

### 🌐 Web Interface
```bash
python3 app.py
```
- Open browser: `http://your-pi-ip:5000`
- Beautiful chat interface
- Real-time health monitoring
- Mobile-friendly

### 💻 Terminal Interface
```bash
python3 terminal_chat.py
```
- Simple command-line chat
- Type `health` to check connection
- Type `quit` to exit

## 🔧 Configuration

### Find Your Laptop IP
On your laptop, run:
```bash
# Windows
ipconfig

# Linux/Mac
ip addr show
```

Update `config.py` with the IP address.

## 📱 Usage Examples

### Web Interface
1. Open `http://your-pi-ip:5000`
2. Type: "What is artificial intelligence?"
3. Get instant responses from your AI Brain

### Terminal Interface
```
You: Hello AI
🧠 AI Brain: Hello! How can I help you today?

You: What's the weather like?
🧠 AI Brain: I'd be happy to help with weather information...

You: health
✅ AI Brain Status: ONLINE

You: quit
👋 Goodbye!
```

## 🛠️ Troubleshooting

### Connection Issues
1. Check if AI Brain is running on laptop
2. Verify laptop IP in `config.py`
3. Test connection: `ping YOUR_LAPTOP_IP`
4. Check firewall settings

### Port Issues
- Web interface uses port 5000
- AI Brain uses port 8000
- Make sure ports are not blocked

## 🔒 Security Notes

- Only use on trusted networks
- Change default ports if needed
- Consider VPN for remote access

## 📋 Requirements

- Raspberry Pi with Python 3.6+
- Network connection to laptop
- AI Brain System running on laptop

## 🎯 Features

- ✅ Real-time chat with AI Brain
- ✅ Health monitoring
- ✅ Web and terminal interfaces
- ✅ Mobile-responsive design
- ✅ Error handling and reconnection
- ✅ Easy configuration

## 🤝 Support

If you encounter issues:
1. Check the AI Brain is running: `curl http://LAPTOP_IP:8000/health`
2. Verify network connectivity
3. Check the logs for error messages

---

**Ready to chat with your AI Brain!** 🧠✨