#!/usr/bin/env python3
import sys
import socket
import base64
from Colors import Colors
from TrafficFactory.DNS import DNS_Factory

def start_string(recv_data):
    maxEnd = 12
    while True:
        cByte = recv_data[maxEnd]
        if cByte != 0: 
            maxEnd += int(cByte)+1
        else:
            maxEnd += 5
            break
    return maxEnd

if __name__ == "__main__":
    dnsFrame = DNS_Factory()
    server_ip = input("IP address: ")  
    port = int(input("Port: "))  
    message = input("Message: ")  

    
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((server_ip, port))  # Use user-provided IP and port

    encoded_message = base64.b85encode(message.encode('utf-8'))  # Encode the message
    client.send(dnsFrame.build_reply_header(dnsFrame.DNS_query_example, encoded_message))  # Send the encoded message

    recv_data = client.recv(512)  # Receive response from the server
    rawString, _ = dnsFrame.dissect_query_data(recv_data[start_string(recv_data):])

    # Decode and print the extracted message
    print(f"{Colors.GREEN}[*] Message successfully sent to {server_ip}:{port}{Colors.END}")
    
    