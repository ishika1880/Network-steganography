#!/usr/bin/env python3
import os
import socket
import struct
import subprocess
import sys
import threading
import base64

from TrafficFactory import DNS

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'

class NetCloak:
    def __init__(self):
        self.clear_screen()
        self.show_banner()
        self.main_menu()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_banner(self):
        banner = f"""{Colors.GREEN}
  _   _      _    ____ _              _    
 | \ | | ___| |_ / ___| | ___  __ __| | __
 |  \| |/ _ \ __| |   | |/   \/ __ | |/ /
 | |\  |  __/ |_| |___| |    || (__|   < 
 |_| \_|\___|\__|\____|_|\___/\____|_|\_\\
    Network Steganography Toolkit
        {Colors.END}"""
        print(banner)

    def main_menu(self):
        while True:
            print(f"\n{Colors.GREEN}Main Menu:{Colors.END}")
            print("1. UDP Steganography")
            print("2. DNS Steganography")
            print("3. HTTP Steganography")
            print("4. Exit")
            
            choice = input("\nSelect protocol (1-4): ")
            
            if choice == "1":
                self.udp_menu()
            elif choice == "2":
                self.dns_menu()
            elif choice == "3":
                self.http_menu()
            elif choice == "4":
                print(f"\n{Colors.GREEN}[*] Thank you for using NetCloak!{Colors.END}")
                sys.exit(0)
            else:
                print(f"\n{Colors.RED}[!] Invalid selection{Colors.END}")

    def udp_menu(self):
        print(f"\n{Colors.RED}[!] UDP operations require administrator privileges!{Colors.END}")
        print(f"{Colors.RED}[!] Please run this script as administrator/sudo{Colors.END}")
        while True:
            print(f"\n{Colors.GREEN}UDP Operations:{Colors.END}")
            print("1. Run UDP Client")
            print("2. Run UDP Server")
            print("3. Return to Main Menu")
            
            choice = input("\nChoose operation (1-3): ")
            
            if choice == "1":
                subprocess.run([sys.executable, "udp_client.py"])
            elif choice == "2":
                subprocess.run([sys.executable, "udp_server.py"])
            elif choice == "3":
                return
            else:
                print(f"{Colors.RED}[!] Invalid choice{Colors.END}")

    def dns_menu(self):
        while True:
            print(f"\n{Colors.GREEN}DNS Operations:{Colors.END}")
            print("1. Run DNS Client")
            print("2. Run DNS Server")
            print("3. Return to Main Menu")
            
            choice = input("\nChoose operation (1-3): ")
            
            if choice == "1":
                subprocess.run([sys.executable, "DNSClient.py"])
            elif choice == "2":
                subprocess.run([sys.executable, "DNSServer.py"])
            elif choice == "3":
                return
            else:
                print(f"{Colors.RED}[!] Invalid choice{Colors.END}")

    def http_menu(self):
        while True:
            print(f"\n{Colors.GREEN}HTTP Operations:{Colors.END}")
            print("1. Run HTTP Client")
            print("2. Run HTTP Server")
            print("3. Return to Main Menu")
            
            choice = input("\nChoose operation (1-3): ")
            
            if choice == "1":
                subprocess.run([sys.executable, "http_exfil.py"])
            elif choice == "2":
                subprocess.run([sys.executable, "http_server.py"])
            elif choice == "3":
                return
            else:
                print(f"{Colors.RED}[!] Invalid choice{Colors.END}")

if __name__ == "__main__":
    NetCloak()
