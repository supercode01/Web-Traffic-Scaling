import requests
import time
import os

# Configuration
PROMETHEUS_URL = "http://localhost:9090/api/v1/query"
QUERY = 'sentinel_predicted_load'
THRESHOLD = 75000000  # Aapke dataset ke mutabiq load (e.g., 800 visits)

def get_prediction():
    try:
        response = requests.get(PROMETHEUS_URL, params={'query': QUERY})
        results = response.json()['data']['result']
        if results:
            return float(results[0]['value'][1])
    except Exception as e:
        print(f"Error fetching data: {e}")
    return 0

def scale_up():
    print("🚀 Surge Predicted! Scaling up to 3 instances...")
    os.system("docker compose up -d --scale web=3")

def scale_down():
    print("📉 Traffic normalized. Scaling down to 1 instance...")
    os.system("docker compose up -d --scale web=1")

print("Sentinel Scaler is active and monitoring...")

while True:
    prediction = get_prediction()
    print(f"Current Prediction: {prediction}")

    if prediction > THRESHOLD:
        scale_up()
    else:
        # Optional: scale down if load is very low
        pass 
    
    time.sleep(10) # Har 10 second baad check karo