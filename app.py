
from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return f"""
        <h2>Flask App Running!</h2>
        <p><strong>Hostname:</strong> <b>{hostname}</b></p>
        <p><strong>IP Address of the Container/pod:</strong> {ip}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
