import socket
import time

data = b"x" * (1024 * 1024)  # 1MB payload

start = time.time()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8888))
s.sendall(data)
s.close()

end = time.time()
print(f"TCP transmission time: {end - start:.4f} seconds")
