
# because i want to call python server_main.py directly
import sys
sys.path.append("..")

import socket

from socket_helper.client_socket import *
from socket_helper.server_socket import *

class TicTacToeClient:
    table = ["" for i in range(9)]

    def __init__(self, server_host):
        self.client_socket = ClientSocket.connect_to_server(server_host, 65001)

    def close(self):
        if self.client_socket != None:
            self.client_socket.close()

    def __del__(self):
        self.close()

if __name__ == "__main__":
    client = TicTacToeClient("127.0.0.1")

    client.close()
