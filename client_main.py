import socket
from socket_helper.client_socket import *
from socket_helper.server_socket import *

# https://realpython.com/python-sockets/
# https://docs.python.org/3/library/socket.html
# https://docs.python.org/3/howto/sockets.html#socket-howto


if __name__ == "__main__":
    s = ClientSocket.connect_to_server("127.0.0.1", 65000)
