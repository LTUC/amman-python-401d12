# serverless function

from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        msg = "welcome from 401 python class"
        self.wfile.write(msg.encode())

        return
