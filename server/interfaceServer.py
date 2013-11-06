'''
Created on 6 sep. 2013

@author: hugo
'''

import socket
import threading
import socketserver
import server.centralController as centralController

def client(ip,port,message):
    '''
    Client function to connect to the
    interface server
    '''
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
    Class that connects with the sniffers and the centralController
    '''
    def __init__(self):
        self.centralController = centralController()
        self.threadedHandler = ThreadedTCPServer(('localhost',12345),ThreadedTCPRequestHandler)
        
    def handle(self,command):
        return self.centralController.userCommand(command)
    
    def close(self,IP,PORT):
        client(IP,PORT,'shutdown')
        self.threadedHandler.shutdown()

'''
if __name__ == "__main__":
    HOST, PORT = "localhost", 25436

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), ThreadedTCPRequestHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
'''    
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 
# sock.sendto(bytes(data + "\n","utf-8"), (HOST, PORT))
# received = str(sock.recv(1024),"utf-8")
# 
# print("Sent:    {}".format(data))
# print("Received {}".format(received))