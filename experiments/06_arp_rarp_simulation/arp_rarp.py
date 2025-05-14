from scapy.all import ARP, Ether, srp

# Function to perform ARP request
def arp_request(target_ip, iface="enp0s1"):
    print(f"Sending ARP request to IP: {target_ip}")

    # Create an ARP request packet (Ethernet + ARP)
    arp_request_packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=target_ip)

    # Send the packet and receive a response
    result = srp(arp_request_packet, timeout=1, iface=iface, verbose=False)[0]

    # Parse the result and print the MAC address of the target
    for sent, received in result:
        print(f"IP: {received.psrc}, MAC: {received.hwsrc}")

# Function to perform RARP request (reverse ARP)
def rarp_request(target_mac, iface="enp0s1"):
    print(f"Sending RARP request for MAC: {target_mac}")

    # Create a RARP request packet (Ethernet + RARP)
    rarp_request_packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=3, hwsrc=target_mac)

    # Send the packet and receive a response
    result = srp(rarp_request_packet, timeout=1, iface=iface, verbose=False)[0]

    # Parse the result and print the IP address for the given MAC
    for sent, received in result:
        print(f"MAC: {received.hwsrc}, IP: {received.psrc}")

# Example of ARP and RARP requests
if __name__ == "__main__":
    # Update with your correct network interface
    interface = "enp0s1"  # Use the correct interface name here
    target_ip = "192.168.1.1"  # Replace with the target IP address for ARP
    target_mac = "00:11:22:33:44:55"  # Replace with the target MAC address for RARP

    # Sending ARP request
    arp_request(target_ip, iface=interface)

    # Sending RARP request
    rarp_request(target_mac, iface=interface)

