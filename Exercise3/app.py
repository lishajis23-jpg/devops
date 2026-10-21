import random
import socket
from flask import Flask, jsonify

app = Flask(__name__)

ITEMS = ["Laptop", "Headphones", "Smartwatch", "Camera", "Tablet"]


@app.route("/")
def home():
    return "Welcome to the Flash Sale! Served by pod: " + socket.gethostname() + "\n"


@app.route("/buy")
def buy():
    return jsonify(item=random.choice(ITEMS), pod=socket.gethostname())


@app.route("/health")
def health():
    return "ok", 200
