import socket
import time

data = b"x" * (1024 * 1024)  # 1MB payload

start = time.time()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(data, ("127.0.0.1", 9999))

end = time.time()
print(f"UDP transmission time: {end - start:.4f} seconds")
