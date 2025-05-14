import pyshark

def capture_and_analyze_packets(interface='enp0s1', packet_count=5, pcap_file='capture.pcap'):
    # Start capturing packets from the specified interface
    capture = pyshark.LiveCapture(interface=interface, output_file=pcap_file)
    
    print(f"Capturing packets on interface: {interface}, saving to {pcap_file}")
    
    packet_num = 0
    # Capture packets continuously until the specified count is reached
    for packet in capture.sniff_continuously():
        if packet_num >= packet_count:
            break
        
        packet_num += 1
        
        # Print packet details while capturing
        print(f"Capturing Packet Number: {packet_num}")
        print(f"Packet Timestamp: {packet.sniff_time}")
        print(f"Packet Length: {packet.length} bytes")
        print(f"Packet Protocol: {packet.highest_layer}")
        print(f"Packet Info: {packet}")
        print("-" * 40)
    
    print(f"Capture complete. {packet_count} packets saved to {pcap_file}.\n")

    # Now, let's analyze the captured .pcap file
    print(f"Analyzing the captured .pcap file: {pcap_file}")
    
    # Read and examine packets from the saved .pcap file
    capture_analyze = pyshark.FileCapture(pcap_file)
    
    for packet_num, packet in enumerate(capture_analyze, 1):
        print(f"Packet Number: {packet_num}")
        print(f"Packet Timestamp: {packet.sniff_time}")
        print(f"Packet Length: {packet.length} bytes")
        print(f"Packet Protocol: {packet.highest_layer}")
        print(f"Packet Info: {packet}")
        print("-" * 40)

if __name__ == "__main__":
    capture_and_analyze_packets('enp0s1', 5, 'capture.pcap')  # Replace 'enp0s1' with the appropriate interface name if needed

