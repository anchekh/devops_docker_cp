from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        message = "<h1>Hello, World!</h1><p>From Python Web Server</p>"
        self.wfile.write(message.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=HelloHandler):
    server_address = ('0.0.0.0', 8000)  # Гость: порт 8000
    httpd = server_class(server_address, handler_class)
    print(f'Server started at http://localhost:8000')
    print('Press Ctrl+C to stop')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
