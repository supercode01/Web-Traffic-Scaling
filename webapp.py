from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Yeh line batayegi ke kaunsa container request handle kar raha hai
    container_id = os.uname()[1] if hasattr(os, 'uname') else "Windows-Machine"
    return f"<h1>Auto-Scale Sentinel: Active</h1><p>Handled by Container: {container_id}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)