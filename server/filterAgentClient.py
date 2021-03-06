'''
Created on 6 sep. 2013

@author: hugo
'''

import socket
import threading
import socketserver
import centralController

def client(ip,port,message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip,port))
    try:
        sock.sendall(message)
        response = sock.recv(1024)
        interfaceServer = interfaceServer()
        interfaceServer.handle(response)
    except:
        sock.close()
                 

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        response = interfaceServer.handle(data)
        self.request.sendall(response)        
class interfaceServer:
    '''
    Class that connects with the sniffer and the centralController
    '''
    def __init__(self):
        self.centralController = centralController()
        self.threadedHandler = ThreadedTCPServer(('localhost',12345),ThreadedTCPRequestHandler)
        
    def handle(self,command):
        return self.centralController.userCommand(command)
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 
# sock.sendto(bytes(data + "\n","utf-8"), (HOST, PORT))
# received = str(sock.recv(1024),"utf-8")
# 
# print("Sent:    {}".format(data))
# print("Received {}".format(received))