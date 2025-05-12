FROM debian:bullseye

# Install packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    sudo \
    iputils-ping \
    net-tools \
    traceroute \
    iproute2 \
    curl \
    netcat \
    nano \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Create user and set password inline
RUN useradd -m -s /bin/bash cnl-container \
    && echo 'cnl-container:cnl123$' | chpasswd \
    && usermod -aG sudo cnl-container

# Set working directory inside container
WORKDIR /home/cnl-container

# Copy files from the current host directory into the container
COPY . /home/cnl-container

# Switch to the new user
USER cnl-container

# Default command
CMD ["bash"]
