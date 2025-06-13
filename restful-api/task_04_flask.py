#!/usr/bin/python3
"""Develop a Simple API using Python with Flask"""

from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Flask API!"


users = {}


@app.route("/data")
def get_user():
    username = list(users.keys())
    return jsonify(username)


@app.route("/status")
def get_status():
    return "OK"


@app.route("/users/<username>")
def get_username(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run()
