
# because i want to call python server_main.py directly
import sys
sys.path.append("..")

import socket

from socket_helper.client_socket import *
from socket_helper.server_socket import *


if __name__ == "__main__":
    server_socket = ServerSocket(65000)

    client_socket = server_socket.wait_for_client()

    while True:
        message = client_socket.recv_string()

        if not message:
            break

        print("Received message: " + message)

        print("Enter reply: ")
        client_socket.send_string(input())

    client_socket.close()
    server_socket.close()
