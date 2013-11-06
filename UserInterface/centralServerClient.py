'''
Created on 8 sep. 2013

@author: hugo
'''
import socket
import pickle
class centralServerClient(object):
    '''
    client object to connect to the central server
    '''
    def __init__(self,IP,PORT):
        '''
        Constructor
        '''
        self.centralIP   = IP
        self.centralPORT = PORT
        self.streamincomingpackets = False
    def connect(self,ip,port):
        self.centralIP = ip
        self.centralPORT = port
        newport = self.client(self.centralIP,self.centralPORT,'client')
        self.centralPORT = int(newport)
        
    def sendRequest(self,request):
        #parse requestdata
        serializedRequest = pickle.dumps(request, pickle.HIGHEST_PROTOCOL)
        self.client(self.centralIP,self.centralPORT,serializedRequest)
    def client(self,ip,port,message):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((ip,port))
        try:
            sock.sendall(message)
            response = sock.recv(4096).decode('utf8').strip()
            return response
        finally:
            sock.close()
            
    