# Simple Chatting App with Python and Tkinter

This repository contains a simple client-server chatting application implemented in Python using the `socket` library for networking and `tkinter` library for the graphical user interface (GUI).

## Server

The server script (`server.py`) sets up a simple chat server that listens for incoming client connections and broadcasts messages between connected clients.

### Usage

Run the server by executing the following command:

```bash
python server.py
```

# Client

The client script (client.py) establishes a connection to the chat server and enables sending and receiving messages.

# Usage

To run multiple clients, execute the following command multiple times:

```bash
python client.py
```

# Dependencies

1. Python 3.9 or higher
2. Tkinter (usually included with standard Python installations)

# How It Works

The server listens for incoming client connections and maintains a list of connected clients. When a client sends a message, the server broadcasts the message to all other connected clients. The client GUI allows users to interact with the server by sending and receiving messages.

