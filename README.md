To build and install your Docker-based CNL lab environment from scratch, follow these complete steps:

⸻

✅ 1. Project Folder Setup

Ensure you have this folder structure:
```
cnl-container-main/
├── Dockerfile
├── analyse_packet.py
├── arp_rarp.py
├── capture_packet.py
├── chat_client.py
├── chat_server.py
├── echo_client.py
├── echo_server.py
└── http_client.py

```

⸻

🐳 2. Build the Docker Image

From inside the cnl-container-main directory:
```
docker build -t cnl-container-image .
```

```
docker build -t cnl-container-image .
docker run -it --name cnl-lab -p 8080:8080 -p 12345:12345 cnl-container-image

```


⸻

🚀 3. Run the Container

To run and expose the necessary ports (8080 and 12345):
```
docker run -it --name cnl-lab -p 8080:8080 -p 12345:12345 cnl-container-image
```
	⚠️ If the container name cnl-lab already exists and you want a new one:
```
docker rm cnl-lab      # Remove old one
docker run -it --name cnl-lab -p 8080:8080 -p 12345:12345 cnl-container-image

```

⸻

🔁 4. Access the Same Container in Two Terminals

Terminal 1:
```
docker start -ai cnl-lab
```
Terminal 2:
```
docker exec -it cnl-lab bash
```


⸻

🧪 5. Try a Test Example (Echo Server & Client)

In Terminal 1 (server):
```
python3 echo_server.py
```
In Terminal 2 (client):
```
python3 echo_client.py
```


⸻

Would you like this bundled as a downloadable README.md file?
