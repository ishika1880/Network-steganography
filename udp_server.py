import socket, struct

ip_address = input("Enter the IP address to bind to: ")
port_number = int(input("Enter the port number to listen on: "))
print("Starting server...")
# Setup socket object
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
s.bind((ip_address, port_number))
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

print("Server running...")

trash_port = 50463
base_port = 47000
stego_message = bytearray()

while (True):
    data = s.recvfrom(65565)
    packet = data[0]
    address = data[1]

    header = struct.unpack('!BBHHHBBH4s4s', packet[14:34])
    msg = packet[28:]
    port = header[4]

    if port == trash_port:
        continue

    if port == base_port - 1:
        if len(stego_message):
            print("Hidden message:", stego_message.decode(errors="ignore"))
        stego_message = bytearray()
        continue

    stego_message.append(port - base_port)