
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

        # TODO: think about better check

        if self.table[0] != "" and self.table[0] == self.table[1] == self.table[2]:
            return TicTacToeServer.who_win(self.table[0])
        elif self.table[3] != "" and self.table[3] == self.table[4] == self.table[5]:
            return TicTacToeServer.who_win(self.table[3])
        elif self.table[6] != "" and self.table[6] == self.table[7] == self.table[8]:
            return TicTacToeServer.who_win(self.table[6])
        elif self.table[0] != "" and self.table[0] == self.table[3] == self.table[6]:
            return TicTacToeServer.who_win(self.table[0])
        elif self.table[1] != "" and self.table[1] == self.table[4] == self.table[7]:
            return TicTacToeServer.who_win(self.table[1])
        elif self.table[2] != "" and self.table[2] == self.table[6] == self.table[8]:
            return TicTacToeServer.who_win(self.table[2])
        elif self.table[0] != "" and self.table[0] == self.table[4] == self.table[8]:
            return TicTacToeServer.who_win(self.table[0])
        elif self.table[2] != "" and self.table[2] == self.table[4] == self.table[6]:
            return TicTacToeServer.who_win(self.table[2])

        return 0

    def start(self):
        # TODO: make code cleaner, check clever after each move

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

                round_result = self.is_finished()

                if round_result == 2:
                    print("You lose")

                    self.client_socket.send_int(round_result + 9)
                    
                    break
            else:
                if round_result == 1:
                    print("You win")
                elif round_result == 2:
                    print("You lose")

                self.client_socket.send_int(round_result + 9)
                self.client_socket.send_int(cell)

                break


if __name__ == "__main__":
    server = TicTacToeServer()
    server.wait_for_tic_tac_toe_client()

    server.start()

    server.close()

