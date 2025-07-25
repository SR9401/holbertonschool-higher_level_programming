#!/usr/bin/python3
"""Develop a Simple API using Python with Flask"""

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    """to handle this route"""

    return "Welcome to the Flask API!"


users = {}


@app.route("/data")
def get_user():
    """return a list of all the usernames stored in the API."""

    username = list(users.keys())
    return jsonify(username)


@app.route("/status")
def get_status():
    """ It should return OK"""

    return "OK"


@app.route("/users/<username>")
def get_username(username):
    """ Returns the full object corresponding to the provided username"""
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Create a new route /add_user that accepts POST requests."""

    r = request.get_json()
    username = r.get("username")

    if not username:

        return jsonify({"error": "Username is required"}), 400
    else:
        users[username] = r
        return jsonify({"message": "User added", "user": r}), 201



if __name__ == "__main__":
    app.run()
