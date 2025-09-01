#!/usr/bin/env python3
import sys
import socket
import base64
from TrafficFactory.DNS import DNS_Factory
import Colors

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
    
    bind_ip = input("Enter the IP address to bind to: ")
    bind_port = int(input("Enter the port number to listen on: "))
    
    print("Starting server...")
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((bind_ip, bind_port))
    print("Server running...")

    while True:
        recv_data, address = server.recvfrom(512)
        print(f'Connection from {address[0]}:{address[1]}')
        rawString, _ = dnsFrame.dissect_query_data(recv_data[start_string(recv_data):])
        print("Hidden message:", base64.b85decode(rawString[0]).decode())
        replyStr = f'Welcome {address[0]}, message received!'
        message = base64.b85encode(replyStr.encode('utf-8'))
        server.sendto(dnsFrame.build_reply_header(dnsFrame.DNS_query_example, message), address)