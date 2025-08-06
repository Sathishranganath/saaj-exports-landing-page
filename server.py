#!/usr/bin/env python3
import http.server
import socketserver
import os

# Change to the directory containing the HTML files
os.chdir('/workspace/project')

PORT = 12000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('X-Frame-Options', 'ALLOWALL')
        super().end_headers()

with socketserver.TCPServer(("0.0.0.0", PORT), MyHTTPRequestHandler) as httpd:
    print(f"Server running at http://0.0.0.0:{PORT}/")
    print(f"Access the website at: https://work-1-boedvdflhdktjozt.prod-runtime.all-hands.dev")
    httpd.serve_forever()