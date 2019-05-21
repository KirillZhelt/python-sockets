
# because i want to call python server_main.py directly
import sys
sys.path.append("..")

import socket

from socket_helper.client_socket import *
from socket_helper.server_socket import *

class TicTacToeServer:
    table = ["" for i in range(9)]

    def __init__(self):
        self.server_socket = ServerSocket(65001)

    def close(self):
        if self.server_socket != None:
            self.server_socket.close()

        if self.client_socket != None:
            self.client_socket.close()

    def __del__(self):
        self.close()

    def wait_for_tic_tac_toe_client(self):
        self.client_socket = self.server_socket.wait_for_client()

    def show_table(self):
        print()
        print("Current table:")

        for i in range(3):
            print(self.table[3 * i], self.table[3 * i + 1], self.table[3 * i + 2])

        print()
    

if __name__ == "__main__":
    server = TicTacToeServer()
    server.wait_for_tic_tac_toe_client()

    server.show_table()

    server.close()

