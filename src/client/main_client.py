import socket


class Client():
    def __init__(self):
        self.hostip = "127.0.0.1"
        self.hostport = 5555

        self.client_socket = None

    def connect_to_server(self):
        # Script to connect to the server
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.hostip, self.hostport))
        print(f"Connected to server: {self.hostip}:{self.hostport}")

    def receive_message(self):
        return self.client_socket.recv(1024).decode()

    def send_message(self, message):
        self.client_socket.send(message.decode())

    def start_chat(self):
        # Makes the user input + gets the data from other guys.
        while True:
            incoming_message = self.receive_message()
            print(f"Server: {incoming_message}")

            #Get user input for new message
            message = input("You: ")
            self.send_message(message)

            if message.lower() == "bye":
                break

        print("Chat ended!")
        self.client_socket.close()



if __name__ == "__main__":
    client = Client()
    client.connect_to_server()
    client.receive_message()
