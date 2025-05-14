```bash
 _          _     _        _                     
| |    __ _| |__ | |_ __ _(_)_ __   ___ _ __ ___ 
| |   / _` | '_ \| __/ _` | | '_ \ / _ \ '__/ __|
| |__| (_| | |_) | || (_| | | | | |  __/ |  \__ \
|_____\__,_|_.__/ \__\__,_|_|_| |_|\___|_|  |___/
```
                                                 
# Computer Networks Laboratory with Labtainers

### An Opensourse initiative by Labtainers

## License

This project is licensed under the BSD-3-Clause license.

---

## Project Folder Structure

Ensure your project folder looks like this:

```
cnl-container-main/
├── Dockerfile
├── LICENSE
├── README.md
└── experiments
    ├── 01_network_tools
    ├── 02_http_client
    ├── 03_tcp_apps
    ├── 04_dns_simulation
    ├── 05_packet_analysis
    ├── 06_arp_rarp_simulation
    ├── 07_congestion_control_sim
    ├── 08_tcp_udp_performance
    ├── 09_routing_algorithms
    └── 10_crc_error_correction
```

---

## How to Set Up and Run the CNL Lab Environment

### Step 1: Project Folder Setup

Make sure your project folder has the following files and structure:

```
.
├── Dockerfile
├── LICENSE
├── README.md
└── experiments
    ├── 01_network_tools
    │   └── 01README.md
    ├── 02_http_client
    │   └── http_client.py
    ├── 03_tcp_apps
    │   ├── chat_client.py
    │   ├── chat_server.py
    │   ├── echo_client.py
    │   └── echo_server.py
    ├── 04_dns_simulation
    │   ├── dns_client.py
    │   └── dns_server.py
    ├── 05_packet_analysis
    │   ├── analyse_packet.py
    │   └── capture_packet.py
    ├── 06_arp_rarp_simulation
    │   └── arp_rarp.py
    ├── 07_congestion_control_sim
    │   ├── stop_and_wait_client.py
    │   └── stop_and_wait_server.py
    ├── 08_tcp_udp_performance
    │   ├── tcp_client.py
    │   ├── tcp_server.py
    │   ├── udp_client.py
    │   └── udp_server.py
    ├── 09_routing_algorithms
    │   ├── dijkstra.py
    │   └── distance_vector.py
    └── 10_crc_error_correction
        └── crc_simulation.py


```

---

### Step 2: Build the Docker Image

From inside the `cnl-container-main` directory, run the following command to build the Docker image:

```bash
docker build -t cnl-container-image .
```

After the build completes, run the container:

```bash
docker run -it --name cnl-lab -p 8080:8080 -p 12345:12345 cnl-container-image
```

---

### Step 3: Run the Container

To run the container and expose the necessary ports (8080 and 12345):

```bash
docker run -it --name cnl-lab -p 8080:8080 -p 12345:12345 cnl-container-image
```

⚠️ If the container with the name `cnl-lab` already exists, you can remove the old one and start fresh:

```bash
docker rm cnl-lab      # Remove the old container
docker run -it --name cnl-lab -p 8080:8080 -p 12345:12345 cnl-container-image
```

---

### Step 4: Access the Same Container in Two Terminals

#### Terminal 1 (Start the container):

```bash
docker start -ai cnl-lab
```

#### Terminal 2 (Access the container's shell):

```bash
docker exec -it cnl-lab bash
```

---

### Step 5: Try a Test Example (Echo Server & Client)

#### In Terminal 1 (Server):

```bash
python3 experiments/03_tcp_apps/echo_server.py
```

#### In Terminal 2 (Client):

```bash
python3 experiments/03_tcp_apps/echo_client.py
```

---

This will test a basic echo server-client setup within the Docker container.

---

