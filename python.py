import http.server
import socketserver

PORT = 8000  # You can choose any available port number

# Define a simple request handler
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, World!")

# Create a TCP/IP server
with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print("Server running at localhost:{}".format(PORT))
    # Start the server
    httpd.serve_forever()
