
# because i want to call python server_main.py directly
import sys
sys.path.append("..")

from tic_tac_toe import TicTacToe

from socket_helper.client_socket import *
from socket_helper.server_socket import *


class TicTacToeClient(TicTacToe):

    mark = "o"

    def __init__(self, server_host):
        TicTacToe.__init__(self)

        self.client_socket = ClientSocket.connect_to_server(server_host, 65001)

    def close(self):
        if self.client_socket != None:
            self.client_socket.close()

    def __del__(self):
        self.close()

    def enter(self):

        while True:
            server_cell = self.client_socket.recv_int()

            if server_cell <= 9:
                self.move(server_cell, "x")
                self.show_table()         

            if server_cell > 9:
                if server_cell == 10 or server_cell == 12:
                    last_server_cell = self.client_socket.recv_int()

                    if last_server_cell != None:
                        self.move(last_server_cell, "x")

                self.show_table()         

                if server_cell == 10:
                    print("You lose")
                elif server_cell == 11:
                    print("You win")
                elif server_cell == 12:
                    print("Draw")

                break

            cell = int(input("Choose a cell (from 1 to 9): "))

            assert 1 <= cell <= 9

            self.move(cell, self.mark)

            self.show_table()
            self.client_socket.send_int(cell)


if __name__ == "__main__":
    server_host = input("Enter server host: ")

    client = TicTacToeClient(server_host)

    client.enter()

    client.close()
