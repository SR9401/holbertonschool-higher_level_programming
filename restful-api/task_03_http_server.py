#!/usr/bin/python3
""" Develop a simple API using Python with the `http.server` module"""

import http.server
import json

class Serv(http.server.BaseHTTPRequestHandler):

	def do_GET(self):
		"""method to handle GET requests."""
		if self.path == "/":
			self.send_response(200)
			self.send_header("Content-Type", "text/plain")
			self.end_headers()
			self.wfile.write(b"Hello, this is a simple API!")

		elif self.path == "/data":
			self.send_response(200)
			self.send_header("Content-Type", "application/json")
			self.end_headers()
			data = {"name": "John", "age": 30, "city": "New York"}
			self.wfile.write(json.dumps(data).encode())

		elif self.path == "/status":
			self.send_response(200)
			self.send_header("Content-Type", "text/plain")
			self.end_headers()
			self.wfile.write(b"OK")

		elif self.path == "/info":
			self.send_response(200)
			self.send_header("Content-Type", "application/json")
			self.end_headers()
			data = {"version": "1.0", "description": "A simple API built with http.server"}
			self.wfile.write(json.dumps(data).encode())

		else:
			self.send_response(404)
			self.send_header("Content-Type", "text/plain")
			self.end_headers()
			self.wfile.write(b"Endpoint not found")

if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = http.server.HTTPServer(server_address, Serv)
    httpd.serve_forever()
