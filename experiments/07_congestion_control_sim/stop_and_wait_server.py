import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("0.0.0.0", 9999))

print("Server is running...")

expected_seq = 0

while True:
    data, addr = server_socket.recvfrom(1024)
    packet = data.decode()

    if not packet:
        break

    seq, msg = packet.split(",", 1)
    seq = int(seq)

    if seq == expected_seq:
        print(f"Received: {msg} (seq: {seq})")
        ack = f"ACK{seq}"
        expected_seq += 1
    else:
        print(f"Duplicate or out-of-order packet (seq: {seq})")
        ack = f"ACK{expected_seq - 1}"

    server_socket.sendto(ack.encode(), addr)
