from socket import *
import struct
from Colors import Colors
    
ip_address = input("IP address: ")
d_port = int(input("Port: "))
hidden_message = input("Message: ") 

s = socket(AF_INET, SOCK_RAW, IPPROTO_UDP)

s_port_base = 47000
d_port = 9123   # arbitrary destination port
checksum = 0

def send_byte(byte_int):
    udp_header = struct.pack('!HHHH', s_port_base + byte_int, d_port, length, checksum)
    s.sendto(udp_header + str.encode(data), (ip_address, d_port))

stego_message = str.encode(hidden_message)
data = 'string'
length = 8 + len(data)

send_byte(-1) # start transmission

for stego_byte in bytearray(stego_message):
    send_byte(stego_byte)

send_byte(-1) # stop transmission

print(f"{Colors.GREEN}[*] Message successfully sent to {ip_address}:{d_port}{Colors.END}")