#!/usr/bin/env python3
import requests
import os
import sys

class AIBrainTerminal:
    def __init__(self):
        self.laptop_ip = os.getenv('LAPTOP_IP', '10.164.119.220')
        self.ai_brain_url = f"http://{self.laptop_ip}:8000"
        
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        
    def print_header(self):
        print("🧠" + "=" * 58 + "🧠")
        print("           AI BRAIN TERMINAL INTERFACE")
        print("🧠" + "=" * 58 + "🧠")
        print(f"📡 Connected to: {self.ai_brain_url}")
        print("💬 Commands: 'quit', 'health', 'clear'")
        print("-" * 60)
        
    def check_health(self):
        try:
            response = requests.get(f"{self.ai_brain_url}/health", timeout=5)
            if response.status_code == 200:
                print("✅ AI Brain Status: ONLINE")
                return True
            else:
                print("❌ AI Brain Status: ERROR")
                return False
        except Exception as e:
            print(f"❌ Connection Failed: {e}")
            return False
            
    def send_query(self, query):
        try:
            print("🤔 AI Brain thinking...")
            response = requests.post(f"{self.ai_brain_url}/process", 
                                   json={"query": query}, 
                                   timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                ai_response = data.get('response', 'No response received')
                print(f"\n🧠 AI Brain: {ai_response}\n")
            else:
                print("❌ Error: Failed to get response")
                
        except Exception as e:
            print(f"❌ Connection Error: {e}")
    
    def run(self):
        self.clear_screen()
        self.print_header()
        
        if not self.check_health():
            print("⚠️  Warning: AI Brain may not be available")
            print("💡 Make sure your laptop AI Brain is running")
        
        print("\n🚀 Ready! Ask me anything:\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("👋 Goodbye!")
                    break
                elif user_input.lower() == 'health':
                    self.check_health()
                elif user_input.lower() == 'clear':
                    self.clear_screen()
                    self.print_header()
                elif user_input:
                    self.send_query(user_input)
                    
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")

if __name__ == "__main__":
    terminal = AIBrainTerminal()
    terminal.run()