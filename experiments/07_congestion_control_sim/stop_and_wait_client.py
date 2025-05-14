import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(2)

server_address = ("127.0.0.1", 9999)

messages = ["Hello", "How", "Are", "You", "Doing?"]
seq = 0

for msg in messages:
    while True:
        packet = f"{seq},{msg}"
        client_socket.sendto(packet.encode(), server_address)

        try:
            ack, _ = client_socket.recvfrom(1024)
            ack = ack.decode()

            if ack == f"ACK{seq}":
                print(f"ACK received for seq {seq}")
                seq += 1
                break
            else:
                print("Received wrong ACK. Resending...")
        except socket.timeout:
            print("Timeout. Resending...")
