from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <h1>Hello from LilleNiels' Flask on ECS Fargate!</h1>
    <p>Hostname: <b>{socket.gethostname()}</b></p>
    <p>Deployed with GitHub Actions → ECR → ECS Fargate</p>
    <p>LIVE NOV 18 2025 – IT WORKS!</p>
    """

@app.route('/health')
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
