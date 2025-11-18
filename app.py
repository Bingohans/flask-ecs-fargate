from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <h1>Hello from BingoNiels' Flask on ECS Fargate!</h1>
    <p>Container hostname: <b>{socket.gethostname()}</b></p>
    <p>Deployed automatically via GitHub Actions → ECR → ECS</p>
    <p><a href="https://lilleniels.dev">My portfolio</a> | Week 2 project live!</p>
    <hr>
    <small>Push any change → new version live in <60 seconds</small>
    """

@app.route('/health')
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
