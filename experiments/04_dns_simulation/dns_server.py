import socket

# Simulated DNS records
dns_records = {
    "example.com": "93.184.216.34",
    "openai.com": "104.20.19.11",
    "google.com": "142.250.64.78"
}

# Setup server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("0.0.0.0", 5353))

print("DNS Server is running on port 5353...")

while True:
    data, addr = server_socket.recvfrom(1024)
    domain = data.decode().strip()
    print(f"Query received for domain: {domain}")

    ip = dns_records.get(domain, "Domain not found")
    server_socket.sendto(ip.encode(), addr)
