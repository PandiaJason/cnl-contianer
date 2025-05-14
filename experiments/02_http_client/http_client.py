import socket

def download_page(url):
    # Parse the URL to extract the host and path
    if url.startswith("http://"):
        url = url[7:]  # Remove the "http://"
    
    # Split URL into host and path, with default path as "/"
    if "/" in url:
        host, path = url.split("/", 1)
        path = "/" + path
    else:
        host = url
        path = "/"

    # Set up a TCP connection to the host (port 80 for HTTP)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, 80))
        
        # Send HTTP GET request
        request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
        client_socket.send(request.encode())

        # Receive the response
        response = b""
        while True:
            chunk = client_socket.recv(4096)
            if not chunk:
                break
            response += chunk

    # Decode the response to string and return
    return response.decode('utf-8', errors='ignore')

# Main program to run the client
if __name__ == "__main__":
    url = input("Enter URL (e.g., http://example.com): ")
    page_content = download_page(url)
    print("\nDownloaded Webpage Content:\n")
    print(page_content)

