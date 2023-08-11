import socket
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

class Server:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
