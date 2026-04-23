from flask import Flask, jsonify
import joblib
import pandas as pd
from datetime import datetime
from prometheus_client import start_http_server, Gauge

app = Flask(__name__)

# 1. Load the Brain
model = joblib.load('sentinel_model.pkl')

# 2. Define Prometheus Metrics
PREDICTED_LOAD = Gauge('sentinel_predicted_load', 'Predicted web traffic load')
ACTUAL_LOAD = Gauge('sentinel_actual_load', 'Actual simulated web traffic load')

# Global counter for real hits
total_hits = 0

@app.route('/visit')
def visit():
    """
    Stress Test will hit this endpoint.
    Each hit will be represented as 100,000 virtual users.
    """
    global total_hits
    total_hits += 100000  # 1 hit = 100k users (for Millions of scale)
    ACTUAL_LOAD.set(total_hits)
    return f"Hit registered! Virtual Load: {total_hits}"

@app.route('/predict')
def predict_traffic():
    now = datetime.now()
    input_data = pd.DataFrame([[now.weekday(), now.month, now.day]], 
                              columns=['day_of_week', 'month', 'day'])
    
    prediction = float(model.predict(input_data)[0])
    PREDICTED_LOAD.set(prediction)
    
    print(f"DEBUG: Predicted: {prediction}, Actual Simulated: {total_hits}")
    
    return jsonify({
        "status": "success",
        "predicted_visits": prediction,
        "actual_simulated_visits": total_hits,
        "timestamp": now.strftime("%Y-%m-%d %H:%M:%S")
    })

if __name__ == '__main__':
    # Start Prometheus client on 8000
    start_http_server(8000)
    # Flask app on 5000
    app.run(host='0.0.0.0', port=5000)