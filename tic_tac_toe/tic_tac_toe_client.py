
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

    def show_table(self):
        print()
        print("Current table:")

        for i in range(3):
            print(self.table[3 * i], self.table[3 * i + 1], self.table[3 * i + 2])

        print()

if __name__ == "__main__":
    client = TicTacToeClient("127.0.0.1")

    client.close()
