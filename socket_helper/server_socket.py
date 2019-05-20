import socket


class ServerSocket:

    def __init__(self, port):
        self.port = port

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.s.listen(1)

    def wait_for_client(self):
        return self.s.accept()



if __name__ == "__main__":
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     s.bind((HOST, PORT))
    #     s.listen()

    #     conn, addr = s.accept()
    #     with conn:
    #         print("Connected by", addr)
    #         while True:
    #             data = conn.recv(1024)
    #             if not data:
    #                 break
    #             conn.sendall(data)
    pass