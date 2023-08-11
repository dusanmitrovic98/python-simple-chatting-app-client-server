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

class MessagingApp:
    def __init__(self, root, client):
        self.root = root
        self.client = client

        self.root.title("Simple Messaging App")

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
        self.text_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.entry = Entry(root)
        self.entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")  # Use sticky="ew"

        self.send_button = Button(root, text="Send", command=self.send_message)
        self.send_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        root.columnconfigure(0, weight=1)  # Make column 0 expand with window width
        root.columnconfigure(1, weight=1)  # Make column 1 expand with window width
