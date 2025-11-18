from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <h1>Hello from LilleNiels' Flask on AWS ECS Fargate!</h1>
    <p>Hostname: <b>{socket.gethostname()}</b></p>
    <p>Public IP: <b>{os.popen('curl -s ifconfig.me').read().strip() or 'unknown'}</b></p>
    <p>Deployed with GitHub Actions → ECR → ECS Fargate → ALB</p>
    <p>LIVE NOV 18 2025 – IT FINALLY WORKS!</p>
    """

@app.route('/health')
def health():
    return {"status": "healthy": "200"}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
