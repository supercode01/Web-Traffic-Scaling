from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    # This line tells us which container is handling the request, useful for debugging in a scaled environment
    container_id = os.uname()[1] if hasattr(os, 'uname') else "Windows-Machine"
    return f"<h1>Auto-Scale Sentinel: Active <p>Handled by Container: {container_id}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)