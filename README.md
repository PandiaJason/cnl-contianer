
🚀 CNL Lab Docker Container

A self-contained Debian-based Docker environment for Computer Networks Lab (CNL) activities. Includes essential networking tools like ping, netstat, traceroute, tcpdump, ifconfig, etc.

⸻

📦 Installed Tools
	•	python3, pip
	•	ping, net-tools, traceroute, iproute2
	•	curl, netcat, nano
	•	build-essential
	•	sudo

⸻

📁 Project Structure

``` bash
.
admin@Jasons-MacBook-Pro cnl-contianer-main % tree
.
├── Dockerfile
├── analyse_packet.py
├── arp_rarp.py
├── capture_packet.py
├── chat_client.py
├── chat_server.py
├── echo_client.py
├── echo_server.py
└── http_client.py

1 directory, 9 files
admin@Jasons-MacBook-Pro cnl-contianer-main % 
```


⸻

🛠️ Step-by-Step Setup

1. Clone the repository

git clone https://github.com/yourusername/cnl-container.git
cd cnl-container



⸻

2. Build the Docker Image

docker build -t cnl-container-image .



⸻

3. Run the Container

docker run -it --name cnl-lab -p 8080:8080 -p 12345:12345 cnl-container-image

	This will:
		•	Start the container named cnl-lab
	•	Expose ports 8080 and 12345
	•	Drop into a bash shell inside the container

⸻

4. Open Second Terminal into Same Container

Keep container running (add tail -f /dev/null to Dockerfile if needed), then open another terminal:

docker exec -it cnl-lab bash

	Now you have two terminals inside the same container!

⸻

5. Stop and Remove Container

docker stop cnl-lab
docker rm cnl-lab



⸻

🔁 Rebuilding & Running Again

If you make changes to code or Dockerfile:

docker build -t cnl-container-image .
docker run -it --name cnl-lab-v2 -p 8080:8080 -p 12345:12345 cnl-container-image

(Use a different name like cnl-lab-v2 if the previous one still exists.)

⸻

📝 Notes
	•	To keep the container alive after closing terminal, consider using:

docker run -dit --name cnl-lab -p 8080:8080 -p 12345:12345 cnl-container-image


	•	Then enter anytime using:

docker exec -it cnl-lab bash


