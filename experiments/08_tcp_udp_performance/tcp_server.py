import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 8888))
s.listen(1)
print("TCP Server listening on port 8888")

conn, addr = s.accept()
data = conn.recv(1024 * 1024)
print(f"Received {len(data)} bytes via TCP")
conn.close()
s.close()
