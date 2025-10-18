# 🧠 AI Brain Pi Frontend Configuration

# UPDATE THIS WITH YOUR LAPTOP'S IP ADDRESS
LAPTOP_IP = "10.164.119.220"

# AI Brain connection settings
AI_BRAIN_PORT = 8000
AI_BRAIN_URL = f"http://{LAPTOP_IP}:{AI_BRAIN_PORT}"

# Pi Frontend settings
PI_FRONTEND_PORT = 5000
PI_FRONTEND_HOST = "0.0.0.0"

# Timeout settings (seconds)
CONNECTION_TIMEOUT = 5
QUERY_TIMEOUT = 30

print(f"🔧 Configuration loaded:")
print(f"📡 AI Brain URL: {AI_BRAIN_URL}")
print(f"🌐 Pi Frontend: http://{PI_FRONTEND_HOST}:{PI_FRONTEND_PORT}")