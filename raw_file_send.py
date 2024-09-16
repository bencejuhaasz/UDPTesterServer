import socket
import argparse
import time



def send_udp_packet(address, port, type, times,time_sleep):
    file_path = "packet_bin_dumps/len_" + str(type) + ".bin"
    # Read packet data from file
    with open(file_path, 'rb') as file:
        packet_data = file.read()

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        for i in range(times):
            # Send packet data
            print(f"Sending packet data from {file_path} to {address}:{port}")
            sent = sock.sendto(packet_data, (address, port))
            time.sleep(time_sleep)
    finally:
        # Close the socket
        sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send data from binary dumps via UDP.")
    parser.add_argument("--ip", required=True, help="IP address to send the packets to")
    parser.add_argument("--port", type=int, required=True, help="Port number to send the packets to")
    args = parser.parse_args()

    address = args.ip
    port = args.port
    # send pattern emulator loop
    while True:
        #------first type of loop
        send_udp_packet(address, port, 45, 35,0.1)
        send_udp_packet(address, port, 644, 1,0)
        send_udp_packet(address, port, 1306, 1,0)
        send_udp_packet(address, port, 1107, 1,0)
        send_udp_packet(address, port, 953, 1,0)
        send_udp_packet(address, port, 231, 1,0)
        send_udp_packet(address, port, 1131, 1,0)
        send_udp_packet(address, port, 1349, 1,0)
        send_udp_packet(address, port, 217, 1,0)
        send_udp_packet(address, port, 1352, 1,0)
        send_udp_packet(address, port, 1239, 1,0)
        #--------------------------------------------