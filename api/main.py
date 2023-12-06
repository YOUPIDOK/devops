import os
import mysql.connector
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Récupérer les informations de connexion à la base de données depuis les variables d'environnement
api_port = os.environ.get('API_PORT', '8000')

db_host = os.environ.get('DB_HOST', 'localhost')
db_port = os.environ.get('DB_PORT', '3306')
db_user = os.environ.get('DB_USER', 'root')
db_password = os.environ.get('DB_PASSWORD', 'password')
db_database = os.environ.get('DB_DATABASE', 'iterator-db')

class DatabaseHandler:
    def get_iterator_value():
        try:
            conn = mysql.connector.connect(
                host=db_host,
                port=db_port,
                user=db_user,
                password=db_password,
                database=db_database
            )
            cursor = conn.cursor()
            cursor.execute('SELECT state FROM interator ORDER BY id DESC LIMIT 1')
            result = cursor.fetchone()
            conn.close()
            return result[0] if result else 0
        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")
            return 0

    def update_iterator_value(value):
        try:
            conn = mysql.connector.connect(
                host=db_host,
                port=db_port,
                user=db_user,
                password=db_password,
                database=db_database
            )
            cursor = conn.cursor()
            cursor.execute('INSERT INTO interator (state) VALUES (%s)', (value,))
            conn.commit()
            conn.close()
        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")

class RequestHandler(BaseHTTPRequestHandler):
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
            iterator_value = DatabaseHandler.get_iterator_value()
            response = 'iterator: ' + str(iterator_value)
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
                    DatabaseHandler.update_iterator_value(value)
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
    server_address = ('127.0.0.1', api_port)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Serveur HTTP démarré sur 127.0.0.1:8000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
