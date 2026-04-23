🛡️ Auto-Scale Sentinel: AI-Driven Predictive Scaling

🌟 Introduction

Auto-Scale Sentinel is an intelligent DevOps solution designed to keep websites from crashing during traffic spikes. Instead of waiting for a server to get overloaded (Reactive), this system uses Machine Learning to predict when a surge will happen (Proactive). Once a surge is forecasted, the system automatically triggers Docker to spin up extra containers, ensuring the website stays smooth and available.

🚀 How to Run the Project (Step-by-Step)

Follow these steps in order to get the full system running:

Step 1: Start the Infrastructure (The Base)

This starts the monitoring tools (Prometheus & Grafana) and the target website.

Action: Open your terminal in the project folder and run:

docker compose up -d


Why? This sets up the environment where everything lives. You can now visit Grafana at http://localhost:3000.

Step 2: Start the AI Sentinel (The Brain)

This activates the ML model to start giving traffic predictions.

Action: Open a new terminal and run:

python app.py

Why? This file loads the AI model and sends the "Predicted Traffic" numbers to Prometheus.

Step 3: Start the Auto-Scaler (The Action)

This script acts as the bridge between the AI and Docker.

Action: Open a new terminal and run:

python scaler.py


Why? It constantly checks the AI's prediction. If the prediction is high (e.g., > 75 Million), it tells Docker to scale the website from 1 container to 3.

Step 4: Run the Stress Test (The Verification)

This is for the "Big Demo Moment" to show the system handling real load.

Action: Open a final terminal and run:

python stress_test.py


Why? This sends thousands of fake requests to the website. You will see the "Actual Load" line rise in Grafana to match the AI's prediction.

📂 File Descriptions (What does what?)

File Name

Description

Why we run it?

sentinel_model.pkl

The trained Machine Learning model.

It is the "Brain" that knows traffic patterns.

app.py

The Sentinel Flask API.

To load the ML model and export metrics for Prometheus.

scaler.py

The Decision-Maker script.

To monitor metrics and trigger docker compose --scale commands.

webapp.py

The actual website code.

This is the "target" application we are protecting.

docker-compose.yml

The orchestration file.

To define and run all containers (Web, Prometheus, Grafana) together.

prometheus.yml

Configuration for monitoring.

Tells Prometheus where to find the data in app.py.

stress_test.py

The load generator script.

To simulate thousands of users for the demo.

main.yml

GitHub Actions Workflow.

Located in .github/workflows/, it verifies code via CI/CD on every push.

📊 Monitoring Dashboards

Grafana: http://localhost:3000 (User: admin, Pass: admin)

Prometheus: http://localhost:9090

Sentinel API: http://localhost:5000/predict

Target Website: http://localhost:8080 (Standard) or mapped ports.

🛠️ Tech Stack summary

AI: Python, Scikit-learn, Pandas.

DevOps: Docker, Docker Compose, GitHub Actions.

Monitoring: Prometheus, Grafana.

Backend: Flask.

Created with ❤️ for the Auto-Scale Sentinel Project.