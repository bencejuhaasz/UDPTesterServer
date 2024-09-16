# README

## Overview

This repository contains two Python scripts: `raw_file_send.py` and `pcapreplay.py`. These scripts are designed to send network packets using different methods and configurations.

## `raw_file_send.py`

### Description

The `pcapreplay.py` script replays packets from a pcap file, optionally modifying the destination IP address and port. It automatically selects the appropriate network interface for sending the packets.

### Usage

```sh
python pcapreplay.py --pcap-file <PCAP_FILE> [--ip <IP_ADDRESS>] [--port <PORT>]
```

### Arguments

- `--pcap-file`: The path to the pcap file to replay (required).
- `--ip`: The IP address to send the packets to (optional).
- `--port`: The port number to send the packets to (optional).

### Example

```sh
python pcapreplay.py --pcap-file capture.pcap --ip 192.168.1.100 --port 8080
```

### Functionality

- Loads packets from the specified pcap file.
- Optionally modifies the destination IP address and port of the packets.
- Automatically selects the default network interface for sending the packets.

## Dependencies

Both scripts require the following Python packages:

- `scapy`
- `argparse`

You can install the required packages using pip:

```sh
pip install scapy argparse
```




### Description

The `raw_file_send.py` script sends UDP packets from binary dump files to a specified IP address and port. It allows for sending multiple packets with specified delays between them.

### Usage

```sh
python raw_file_send.py --ip <IP_ADDRESS> --port <PORT>
```

### Arguments

- `--ip`: The IP address to send the packets to (required).
- `--port`: The port number to send the packets to (required).

### Example

```sh
python raw_file_send.py --ip 192.168.1.100 --port 8080
```

### Functionality

- Reads packet data from binary files located in the `packet_bin_dumps` directory.
- Sends the packets to the specified IP address and port.
- Allows for a configurable delay between sending packets.

## `pcapreplay.py`


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.