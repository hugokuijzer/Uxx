'''
Created on 6 sep. 2013

@author: hugo
'''

import socket
import sys

HOST,PORT = "localhost", 9997
data = "  dit is die tekst jo!"
print(data);
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(bytes(data + "\n","utf-8"), (HOST, PORT))
received = str(sock.recv(1024),"utf-8")

print("Sent:    {}".format(data))
print("Received {}".format(received))