import tkinter as tk
from tkinter import scrolledtext, Entry, Button
import socket
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((SERVER_HOST, SERVER_PORT))

    def send_message(self, message):
        self.client_socket.send(message.encode('utf-8'))

    def start_receiving(self):
        while True:
            message = self.client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            app.text_area.insert(tk.END, f"Stranger: {message}\n")
