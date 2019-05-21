
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

    @staticmethod
    def cell_content(s, i):
        if s == "":
            return str(i + 1)

        return s

    def show_table(self):
        print()
        print("Current table:")

        for i in range(3):
            print(TicTacToeServer.cell_content(self.table[3 * i], 3 * i),\
                TicTacToeServer.cell_content(self.table[3 * i + 1], 3 * i + 1),\
                TicTacToeServer.cell_content(self.table[3 * i + 2], 3 * i + 2))

        print()

    @staticmethod
    def who_win(s):
        return 1 if s == "x" else 2

    def is_finished(self):
        # 0 - not finished, 1 - server(x) win, 2 - client(o) win 
        if self.data[0] != "" and self.data[0] == self.data[1] == self.data[2]:
            return TicTacToeServer.who_win(self.data[0])
        elif self.data[3] != "" and self.data[3] == self.data[4] == self.data[5]:
            return TicTacToeServer.who_win(self.data[3])
        elif self.data[6] != "" and self.data[6] == self.data[7] == self.data[8]:
            return TicTacToeServer.who_win(self.data[6])
        elif self.data[0] != "" and self.data[0] == self.data[3] == self.data[6]:
            return TicTacToeServer.who_win(self.data[0])
        elif self.data[1] != "" and self.data[1] == self.data[4] == self.data[7]:
            return TicTacToeServer.who_win(self.data[1])
        elif self.data[2] != "" and self.data[2] == self.data[6] == self.data[8]:
            return TicTacToeServer.who_win(self.data[2])
        elif self.data[0] != "" and self.data[0] == self.data[4] == self.data[8]:
            return TicTacToeServer.who_win(self.data[0])
        elif self.data[2] != "" and self.data[2] == self.data[4] == self.data[6]:
            return TicTacToeServer.who_win(self.data[2])

        return 0

    def start(self):
        while True:
            print("Choose a cell (from 1 to 9): ", end=" ")
            cell = int(input())

            assert 1 <= cell <= 9

            if self.table[cell - 1] != "o":
                self.table[cell - 1] = "x"

            self.show_table()

            round_result = self.is_finished()
            if round_result == 0:
                self.client_socket.send_int(cell)
                client_cell = self.client_socket.recv_int()

                self.table[client_cell - 1] = "o"

                self.show_table()
            else:
                if round_result == 1:
                    print("You win")
                else:
                    print("You lose")

                




if __name__ == "__main__":
    server = TicTacToeServer()
    server.wait_for_tic_tac_toe_client()

    server.start()

    server.close()

