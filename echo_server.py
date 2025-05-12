import socket

def start_server():
    # Set up the server to listen on localhost and port 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server listening on port 12345...")

    while True:
        # Accept a connection from a client
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} established.")

        # Receive data from the client
        data = client_socket.recv(1024)
        print(f"Received: {data.decode()}")

        # Send the same data back (echo)
        client_socket.send(data)

        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    start_server()
