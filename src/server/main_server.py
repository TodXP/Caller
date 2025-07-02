import socket
import threading

# Making a list for the clients to connect to.

clients = {}


# Creating server class
class Server():
    def __init__(self):
        self.hostip = "127.0.0.1" # Default localhost
        self.hostport = 5555

    def start_server(self):
        #Creating a host
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.hostip, self.hostport))
        print(f"{self.hostip}:{self.hostport}")


        print("Server started")


if __name__ == "__main__":
    server = Server()
    server.start_server()