from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <h1>Hej fra LilleNiels' Flask på AWS ECS Fargate!</h1>
    <p>Denne container blev bygget og deployet automatisk med GitHub Actions</p>
    <p>Instance ID: {os.uname().nodename}</p>
    <p><a href="https://bingoniels.space">Min portfolio</a></p>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
