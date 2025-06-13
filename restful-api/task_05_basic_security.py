#!/usr/bin/python3
"""API Security and Authentication Techniques"""

from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
