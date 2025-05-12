import pyshark

def analyze_pcap(file_path):
    # Open the pcap file and analyze the packets
    capture = pyshark.FileCapture(file_path)

    print(f"Analyzing file: {file_path}")

    for packet in capture:
        print(f"Packet Number: {capture.packet_count}")
        print(f"Packet Timestamp: {packet.sniff_time}")
        print(f"Packet Length: {packet.length} bytes")
        print(f"Packet Protocol: {packet.highest_layer}")
        print(f"Packet Info: {packet}")
        print("-" * 40)

if __name__ == "__main__":
    analyze_pcap('example.pcap')  # Replace with your .pcap file path
