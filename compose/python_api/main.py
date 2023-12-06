from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class RequestHandler(BaseHTTPRequestHandler):
    # Valeur d'itérateur (initialement 0)
    iterator_value = 0

    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = ""
        elif self.path == '/get':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = 'iterator: ' + str(self.iterator_value)
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = 'Route not found'
        
        self.wfile.write(response.encode('utf-8'))

    def do_POST(self):
        if self.path == '/add':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                value = data['value']
                if isinstance(value, int):
                    RequestHandler.iterator_value += value
                    self.send_response(200)
                    response = 'Value updated successfully'
                else:
                    self.send_response(400)
                    response = 'Invalid input value (not an integer)'
            except (KeyError, json.JSONDecodeError):
                self.send_response(400)
                response = 'Invalid input format'
        else:
            self.send_response(404)
            response = 'Route not found'
        
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

def run():
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Serveur HTTP démarré sur 127.0.0.1:8000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
