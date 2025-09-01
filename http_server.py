#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from Colors import Colors

hdrs = []

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = "Success!"
        self.wfile.write(bytes(message, "utf8"))
        print(f"{Colors.GREEN}[*] Received request from {self.client_address[0]}{Colors.END}")
        headers = self.headers
        if self.path.endswith('1'):
            hdrs.append(str(headers))
        elif self.path.endswith('0'):
            hdrs.append(str(headers))
            decode_message(hdrs)
            del hdrs[:]

def bin2chr(byte):
    return chr(int(byte, 2))

def read_from_line(line):
    binary = []
    index = line.find(' ')
    while True:
        index = line.find(' ',index+1)
        if index < 0: break
        if line[index+1] == ' ':
            binary.append('1')
            index += 1
        else:
            binary.append('0')
    return ''.join(binary)

def read_from_request(request):
    lines = request.split('\n')
    binary = []
    for line in lines:
        if line.find('\r') < 0:
            line = line + '\r'
        bits = read_from_line(line)
        binary.append(bits)
    return ''.join(binary)

def decode_message(stego_requests):
    binary = []
    message = []
    for req in stego_requests:
        binary.append(read_from_request(req))
    bin_msg = ''.join(binary)
    for i in range(8,len(bin_msg),8):
        message.append(bin2chr(bin_msg[i-8 : i]))
    print(''.join(message))

def main():
    ip_address = input("Enter the IP address to bind to: ")
    port_number = int(input("Enter the port number to listen on: "))
    print('Starting server...')
    server_address = (ip_address, port_number)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('Server running...')
    httpd.serve_forever()

if __name__ == '__main__':
    main()