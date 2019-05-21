
# because i want to call python client_main.py directly
import sys
sys.path.append("..")

import socket

from socket_helper.client_socket import *
from socket_helper.server_socket import *


if __name__ == "__main__":
    print("Enter server host: ")
    server_host = input()

    client_socket = ClientSocket.connect_to_server(server_host, 65000)

    while True:
        print("Enter a message or 'quit' to quit: ")
        message = input()

        if message == "quit":
            break

        client_socket.send_string(message)
        print("Received reply: " + client_socket.recv_string())

    client_socket.close()


    
