import socket

def start_client():
    # Create a socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Send a message to the server
    message = "Hello, Server!"
    client_socket.send(message.encode())

    # Receive the echoed message from the server
    data = client_socket.recv(1024)
    print(f"Received from server: {data.decode()}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()
