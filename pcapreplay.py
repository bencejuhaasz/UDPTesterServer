import logging
from scapy.all import rdpcap, IP, sendp, conf
from scapy.arch.windows import get_windows_if_list
import argparse
import socket

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def list_interfaces():
    interfaces = get_windows_if_list()
    for iface in interfaces:
        logging.info(f"Name: {iface['name']}, Description: {iface['description']}")

def send_pcap_file(pcap_file, address, port, loop):
    logging.info(f"Loading pcap file: {pcap_file}")
    packets = rdpcap(pcap_file)

    logging.info(f"Rewriting IPs and sending packets to {address}:{port}")
    for packet in packets:
        if IP in packet:
            packet[IP].src = socket.gethostbyname(socket.gethostname())
            packet[IP].dst = address
            if port is not None:
                packet[IP].dport = port
            del packet[IP].chksum

    try:
        if loop:
            while True:
                sendp(packets)
                logging.info(f"Sent {len(packets)} packets")
        else:
            sendp(packets)
            logging.info(f"Sent {len(packets)} packets")
    except KeyboardInterrupt:
        logging.info("Program interrupted by user. Exiting...")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send data from pcap files.")
    parser.add_argument("--ip", required=False, help="IP address to send the packets to")
    parser.add_argument("--port", type=int, required=False, help="Port number to send the packets to")
    parser.add_argument("--pcap-file", required=True, help="Path to the pcap file to replay")
    parser.add_argument("--repeat", action="store_true", help="Repeat sending the packets indefinitely")
    args = parser.parse_args()

    address = args.ip
    port = args.port

    conf.iface = conf.iface

    try:
        if args.repeat:
            send_pcap_file(args.pcap_file, address, port, loop=True)
        else:
            send_pcap_file(args.pcap_file, address, port, loop=False)
    except KeyboardInterrupt:
        logging.info("Program interrupted by user. Exiting...")