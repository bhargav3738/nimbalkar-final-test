from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Final test</title>
    </head>
    <body>
        <h1>Welcome to Nimbalkar Final Test API Server</h1>
    </body>
    </html>
    """
    return html_content

@app.route('/host')
def get_host():
    hostname = socket.gethostname()
    return f"Hostname: {hostname}"

@app.route('/ip')
def get_ip():
    ip_address = request.remote_addr
    return f"Your IP Address: {ip_address}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
