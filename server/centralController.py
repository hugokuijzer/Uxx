'''
Created on 8 sep. 2013

@author: hugo
'''
import queue
import DBController
import interfaceServer
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
        self.interfaceServer = interfaceServer
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
            interfaceServer.close(close)
            interfaceServer.succes()
            
        
    def snifferReturn(self,command):
        '''
        Packet was returned from the sniffer, send to 
        the DB and to the interface module
        '''
        self.databaseQueue.put(command)
        self.interfaceQueue.put(command)
    
import DBController
class databaseThread(Thread, DBController DBcontrol):
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
    def process(self,command,*params):
        if (command == "Get")
            return DBcontrol.Get()
        elif (command == "Get_One")
            return DBcontrol.Get_One(params)
        elif (command == "Get_Documents")
            return DBcontrol.Get(params)
        elif (command == "Set")
            return DBcontrol.Set(params)
        elif (command == "Set_Documents")
            return DBcontrol.Set_Documents(params)
        elif (command == "Create_Document")
            return DBcontrol.Create_Document(params[0],params[1])
        elif (command == "Create_IPDocument")
            return DBcontrol.Create_IPDocument(params[0],params[1],params[2])
        elif (command == "Create_TCPDocument")
            return DBcontrol.Create_TCPDocument(params[0],params[1],params[2])
        elif (command == "Create_DNSDocument")
            return DBcontrol.Create_DNSDocument()
        #elif (command == "Create_Documents")
        #   return DBcontrol.Create_Documents()
        
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