import socket
import threading

# Making a list for the clients to connect to.


# Creating server class
class Server():
    def __init__(self):
        self.hostip = "127.0.0.1" # Default localhost
        self.hostport = 5555

        self.clients = []

    def handle_client(self, client_socket, client_address):
        #Try's to handle all the clients at the same time.
        try:
            while True:
                message = client_socket.recv(1024).decode()
                if message.lower() == "bye":
                    client_socket.send("Ending the chat\n".encode())
                if message:
                    print(f"{client_address}: {message}")
                    self.relay_message(client_socket, message)
        except Exception as e:
            print(f"Got error {e}")
        finally:
            self.remove_client(client_socket)
            

    def remove_client(self, client_socket):
        self.clients.remove(client_socket)
        client_socket.close()

    def relay_message(self, sender_socket, message):
        for client_socket in self.clients:
            if client_socket != sender_socket:
                client_socket.send(message.encode())

    def add_client(self, client_socket):
        #Adding a client to the list
        self.clients.append(client_socket)

    def start_server(self):
        #Creating a host
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.hostip, self.hostport))
        print(f"{self.hostip}:{self.hostport}")

        server_socket.listen(5)

        while True:
            # Adding clients
            client_socket, client_address = server_socket.accept()
            print(f"Added a new user: {client_address}")


if __name__ == "__main__":
    server = Server()
    server.start_server()