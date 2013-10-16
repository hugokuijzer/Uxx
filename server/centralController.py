'''
Created on 8 sep. 2013

@author: hugo
'''
import queue
import socket
import server.DBController.DBController as DBController
import server.interfaceServer as interfaceServer
import threading


class centralController:
    '''
Central controller class that links the server request from the user interface to request
made by the filterAgent client and makes sure that all data is properly stored in the database
    ''' 
    def __init__(self):
        '''
        Constructor
        '''
        self.databaseQueue = queue.Queue
        self.interfaceQueue = queue.Queue
        self.snifferQueue   = queue.Queue
        self.interfaceServer = interfaceServer
        #connectionList holds the from IP as key and the to as value
        #both in a string
        self.connectionList = {}
        self.start()
        
    def start(self):
        pass
        
    def userCommand(self,command):
        '''
        A new command was received from the user
        process it!
        '''
        if command.command == "new connection": 
            self.databaseQueue.put(command)
            self.snifferQueue.put(command)
            self.connectionList[command.fromIP] = command.toIP
        elif command.command == "close connection":
            close = self.connectionList.pop(command.fromIP)
            interfaceServer.close(close)
            interfaceServer.succes()
            
        
    def snifferReturn(self,command):
        '''
        Packet was returned from the sniffer, send to 
        the DB and to the interface module
        '''
        self.databaseQueue.put(command)
        self.interfaceQueue.put(command)
    

class databaseThread(threading.Thread, DBController):
    '''
    These threads will send all necessary data to the 
    database controller
    '''
    def __init__(self,queue):
        threading.Thread.__init__()
        self.queue = queue
    def start(self):
        while True:
            command  = self.queue.get()
            dbReturn = self.process(command)
            self.queue.task_done()
    def process(self,command,*params):
        if (command == "Get"):
            return DBController.Get()
        elif (command == "Get_One"):
            return DBController.Get_One(params)
        elif (command == "Get_Documents"):
            return DBController.Get(params)
        elif (command == "Set"):
            return DBController.Set(params)
        elif (command == "Set_Documents"):
            return DBController.Set_Documents(params)
        elif (command == "Create_Document"):
            return DBController.CreateDocument(params[0],params[1])
        elif (command == "Create_IPDocument"):
            return DBController.CreateIPDocument(params[0],params[1],params[2])
        elif (command == "Create_TCPDocument"):
            return DBController.CreateTCPDocument(params[0],params[1],params[2])
        elif (command == "Create_DNSDocument"):
            return DBController.CreateDNSDocument(params[0],params[1],params[2])
        #elif (command == "Create_Documents")
        #   return DBController.Create_Documents()
        
class interfaceThread(threading.Thread):
    '''
    These thread will send data back to and from the interface
    '''
    def __init__(self,queue):
        threading.Thread.__init__()
        self.queue = queue
    def start(self):
        while True:
            command = self.queue.get()
            interfaceReturn = self.process(command)
            self.queue.task_done()
    def process(self,command):
        pass
    
class snifferThread(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__()
        self.queue = queue
    def start(self):
        while True:
            command = self.queue.get()
            snifferReturn = self.process(command)
            self.queue.task_done()
    def process(self,command):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM,command)
        try:
            sock.connect((command.destIP,command.destPort))
            sock.sendall(command)
            response = sock.recv(4096)
        finally:
            sock.close()
def main():
    centralController = centralController()
    centralController.start()
if __name__ == "__main__":
    main()