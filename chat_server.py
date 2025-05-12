import socket
import threading

# Function to handle each client connection
def handle_client(client_socket):
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"Client: {message.decode()}")
            
            # Send the message back (echo)
            client_socket.send(f"Server: {message.decode()}".encode())
        except:
            break

    # Close the connection when done
    client_socket.close()

# Function to start the server
def start_server():
    # Set up the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server listening on port 12345...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} established.")
        
        # Start a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
