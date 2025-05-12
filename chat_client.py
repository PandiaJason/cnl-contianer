import socket

# Function to send and receive messages
def start_client():
    # Create a socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    while True:
        # Get user input for the message
        message = input("You: ")
        if message.lower() == 'exit':
            break

        # Send the message to the server
        client_socket.send(message.encode())

        # Receive the server's response
        response = client_socket.recv(1024)
        print(response.decode())

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()
