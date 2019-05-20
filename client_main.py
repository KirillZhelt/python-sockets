import socket
from socket_helper.client_socket import *
from socket_helper.server_socket import *

# https://realpython.com/python-sockets/
# https://docs.python.org/3/library/socket.html
# https://docs.python.org/3/howto/sockets.html#socket-howto

# TODO: handle errors??
# https://www.binarytides.com/receive-full-data-with-the-recv-socket-function-in-python/

if __name__ == "__main__":
    s = ClientSocket.connect_to_server("127.0.0.1", 65000)

    s.send_bytes_msg(b"Hello world")
    s.send_int(-5)
    s.send_float(3.67)
    s.send_string("Hello world")
    s.send_string("Привет мир")
