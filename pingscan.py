#!/usr/bin/python3
# python pingscan.py 192.168.1.1/24
from ipaddress import ip_network
import socket
import time
import sys

def main():
	r = sys.argv[1]
	s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
	s.setblocking(False)
	for i in ip_network(r, strict=False).hosts():
		s.sendto(b"\x08\x00\x4d\x55\x00\x01\x00\x06\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x61\x62\x63\x64\x65\x66\x67\x68\x69", (str(i), 0))

	time.sleep(0.5)
	try:
		while data := s.recvfrom(1024):
			ip = data[1][0]
			if data[0][20] == 0:
				print(ip)

	except BlockingIOError:
		pass

	s.close()

if __name__ == '__main__':
	main()

