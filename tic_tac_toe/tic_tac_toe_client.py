
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

    @staticmethod
    def cell_content(s, i):
        if s == "":
            return str(i + 1)

        return s

    def show_table(self):
        print()
        print("Current table:")

        for i in range(3):
            print(TicTacToeClient.cell_content(self.table[3 * i], 3 * i), \
                TicTacToeClient.cell_content(self.table[3 * i + 1], 3 * i + 1),\
                TicTacToeClient.cell_content(self.table[3 * i + 2], 3 * i + 2))

        print()

    def enter(self):

        while True:
            server_cell = self.client_socket.recv_int()
            self.table[server_cell - 1] = "x"
            self.show_table()         

            print("Choose a cell (from 1 to 9): ", end=" ")
            cell = int(input())

            assert 1 <= cell <= 9

            if self.table[cell - 1] != "x":
                self.table[cell - 1] = "o"

            self.show_table()
            self.client_socket.send_int(cell)


if __name__ == "__main__":
    client = TicTacToeClient("127.0.0.1")

    client.enter()

    client.close()
