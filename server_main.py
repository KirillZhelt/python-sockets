import socket
from socket_helper.client_socket import *
from socket_helper.server_socket import *

# https://realpython.com/python-sockets/
# https://docs.python.org/3/library/socket.html
# https://docs.python.org/3/howto/sockets.html#socket-howto


if __name__ == "__main__":
    s = ServerSocket(65000)

    client = s.wait_for_client()

    print(client.recv_bytes_msg())
    print(client.recv_int())
    print(client.recv_float())
    print(client.recv_string())
    print(client.recv_string())
