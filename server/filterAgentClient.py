'''
Created on 6 sep. 2013

@author: hugo
'''

import socket
import threading
import socketserver
import centralController


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        
class filterAgentClient:
    '''
    Class that connects with the sniffers and the centralController
    '''
    def __init__(self):
        self.centralController = centralController
        self.threadedHandler = ThreadedTCPServer(('localhost',12345),ThreadedTCPRequestHandler)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(bytes(data + "\n","utf-8"), (HOST, PORT))
received = str(sock.recv(1024),"utf-8")

print("Sent:    {}".format(data))
print("Received {}".format(received))