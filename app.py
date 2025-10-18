from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Configuration - Update with your laptop's IP
LAPTOP_IP = os.getenv('LAPTOP_IP', '10.164.119.220')
AI_BRAIN_URL = f"http://{LAPTOP_IP}:8000"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_ai():
    data = request.json
    query = data.get('query', '')
    
    if not query:
        return jsonify({"error": "Query is required"})
    
    try:
        response = requests.post(f"{AI_BRAIN_URL}/process", 
                               json={"query": query}, 
                               timeout=30)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": f"Connection failed: {str(e)}"})

@app.route('/health')
def health():
    try:
        response = requests.get(f"{AI_BRAIN_URL}/health", timeout=5)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": f"AI Brain offline: {str(e)}"})

if __name__ == '__main__':
    print(f"🧠 AI Brain Pi Frontend starting...")
    print(f"📡 Connecting to AI Brain at: {AI_BRAIN_URL}")
    print(f"🌐 Web interface will be available at: http://0.0.0.0:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)