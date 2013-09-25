'''
Created on 8 sep. 2013

@author: hugo
'''
import queue
import DBController
import filterAgentClient
import interfaceServer


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
        self.filterAgentClient = filterAgentClient
        self.interfaceServer   = interfaceServer
        #connectionList holds the from IP as key and the to as value
        #both in a string
        self.connectionList = {}
        self.start()
        
    def start():
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
            filterAgentClient.close(close)
            interfaceServer.succes()
            
        
    def snifferReturn(self,command):
        '''
        Packet was returned from the sniffer, send to 
        the DB and to the interface module
        '''
        self.databaseQueue.put(command)
        self.interfaceQueue.put(command)
        
class databaseThread(Thread):
    '''
    These threads will send all necessary data to the 
    database controller
    '''
    def __init__(self,queue):
        Thread.__init__()
        self.queue = queue
    def start(self):
        while True:
            command  = self.queue.get()
            dbReturn = self.process(command)
            self.queue.task_done()
    def process(self,command):
        '''
        Make something usefull out of the command object
        that can be sent into the database
        '''
class interfaceThread(Thread):
    '''
    These thread will send data back to and from the interface
    '''
    def __init__(self,queue):
        Thread.__init__()
        self.queue = queue
    def start(self):
        pass
    def process(self,command):
        pass
    
class snifferThread(Thread):
    def __init__(self,queue):
        Thread.__init__()
        self.queue = queue
    def start(self):
        pass
    def process(self):
        pass
def main():
    centralController = centralController()
    centralController.start()
if __name__ == "__main__":
    main()