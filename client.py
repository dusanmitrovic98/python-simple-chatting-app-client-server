import tkinter as tk
from tkinter import scrolledtext, Entry, Button
import socket
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
