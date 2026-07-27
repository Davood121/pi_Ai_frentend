# AI Brain Pi Frontend

> Pi AI Frontend - Web-based user interface for AI interaction with Python backend integration.

Raspberry Pi frontend interface for the AI Brain System. Connect your Pi to your laptop's AI Brain and start chatting.

## Features

- **Real-Time Chat** — Instant communication with your AI Brain over the network
- **Health Monitoring** — Live AI Brain status and connection diagnostics
- **Dual Interfaces** — Choose between web UI or terminal-based chat
- **Mobile-Responsive** — Clean interface that works on any device
- **Error Handling** — Automatic reconnection and graceful error recovery
- **Easy Configuration** — Simple IP-based setup with minimal configuration

## Quick Setup

### 1. Download to Raspberry Pi
```bash
git clone https://github.com/Davood121/pi-Ai-frontend.git
cd pi-Ai-frontend
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

## Interface Options

### Web Interface
```bash
python3 app.py
```
- Open browser: `http://your-pi-ip:5000`
- Beautiful chat interface with real-time updates
- Mobile-friendly responsive design

### Terminal Interface
```bash
python3 terminal_chat.py
```
- Simple command-line chat
- Type `health` to check connection
- Type `quit` to exit

## Usage Examples

```
You: What is artificial intelligence?
AI Brain: Hello! How can I help you today?

You: What's the weather like?
AI Brain: I'd be happy to help with weather information...

You: health
AI Brain Status: ONLINE

You: quit
Goodbye!
```

## Configuration

### Find Your Laptop IP
```bash
# Windows
ipconfig

# Linux/Mac
ip addr show
```

Update `config.py` with the laptop's IP address.

## Troubleshooting

### Connection Issues
1. Check if AI Brain is running on laptop
2. Verify laptop IP in `config.py`
3. Test connection: `ping YOUR_LAPTOP_IP`
4. Check firewall settings

### Port Issues
- Web interface uses port 5000
- AI Brain uses port 8000
- Ensure ports are not blocked

## Security Notes

- Only use on trusted networks
- Change default ports if needed
- Consider VPN for remote access

## Requirements

- Raspberry Pi with Python 3.6+
- Network connection to laptop
- AI Brain System running on laptop

## Tech Stack

- **Backend:** Python 3, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Communication:** HTTP / REST API

## Support

If you encounter issues:
1. Check AI Brain is running: `curl http://LAPTOP_IP:8000/health`
2. Verify network connectivity
3. Check the logs for error messages

## Links

- [GitHub Repository](https://github.com/Davood121/pi-Ai-frontend)