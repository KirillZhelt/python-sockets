
# because i want to call python server_main.py directly
import sys
sys.path.append("..")

from tic_tac_toe import TicTacToe

from socket_helper.client_socket import *
from socket_helper.server_socket import *


class TicTacToeServer(TicTacToe):

    mark = "x"

    def __init__(self):
        TicTacToe.__init__(self)

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

    def start(self):

        while True:
            cell = int(input("Choose a cell (from 1 to 9): "))

            assert 1 <= cell <= 9, "cell should be from 1 to 9"

            self.move(cell, self.mark)
            self.show_table()

            round_result = self.is_finished(cell, self.mark)
            if round_result == 0:
                # game is not over

                self.client_socket.send_int(cell)
                client_cell = self.client_socket.recv_int()

                self.move(client_cell, "o")
                self.show_table()

                round_result = self.is_finished(client_cell, "o")

                if round_result == 2:
                    print("You lose")

                    self.client_socket.send_int(round_result + 9)
                    
                    break
                elif round_result == 3:
                    print("Draw")

                    self.client_socket.send_int(round_result + 9)

                    break
            else:
                # game is over
                if round_result == 1:
                    print("You win")
                elif round_result == 3:
                    print("Draw") 

                self.client_socket.send_int(round_result + 9)
                self.client_socket.send_int(cell)

                break


if __name__ == "__main__":
    server = TicTacToeServer()
    server.wait_for_tic_tac_toe_client()

    server.start()

    server.close()

