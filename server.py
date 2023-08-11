import socket
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

class Server:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((SERVER_HOST, SERVER_PORT))
        self.server_socket.listen(5)
        self.clients = []
        print(f"Listening on {SERVER_HOST}:{SERVER_PORT}")

    def start(self):
        while True:
            client_socket, _ = self.server_socket.accept()
            self.clients.append(client_socket)
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
