from flask import Flask
import os
import socket
from waitress import serve

app = Flask(__name__)

# ...existing code...

def find_open_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return port

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", find_open_port()))  # Find an open port if PORT is not set
    serve(app, host="0.0.0.0", port=PORT)