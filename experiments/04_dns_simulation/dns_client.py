import socket

server_ip = "127.0.0.1"  # change if server is on a different machine
server_port = 5353

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

domain = input("Enter domain to resolve (e.g. example.com): ")
client_socket.sendto(domain.encode(), (server_ip, server_port))

data, _ = client_socket.recvfrom(1024)
print("Received IP address:", data.decode())

client_socket.close()
