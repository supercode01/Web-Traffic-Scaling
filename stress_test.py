import requests
import time
import threading

# 1. Asli Website (Bojh dalne ke liye)
WEB_URL = "http://localhost:8080"
# 2. Sentinel API (Metrics update karne ke liye)
METRIC_URL = "http://localhost:5000/visit"

def send_requests():
    while True:
        try:
            # Pehle website ko hit karo (Actual work)
            requests.get(WEB_URL, timeout=1)
            
            # Phir Sentinel ko hit karo (To update Grafana line)
            requests.get(METRIC_URL, timeout=1)
            
        except Exception as e:
            # Agar koi error aaye (jaise server down), toh khamoshi se chalta rahe
            pass

print("🚀 Starting Integrated Stress Test...")
print(f"Targeting Website: {WEB_URL}")
print(f"Updating Metrics: {METRIC_URL}")

# 10 threads kaafi hain. Har thread Sentinel ko hits bhej kar 
# millions ka simulated load generate karega.
for i in range(10):
    thread = threading.Thread(target=send_requests)
    thread.daemon = True
    thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n🛑 Stress test stopped by user.")