'''
Created on 8 sep. 2013

@author: hugo
'''
import UserInterface.centralServerClient as centralServerClient
import FilterAgent.ltcp.dataPacket as dataPacket

class prettyPrinter(object):
    '''
    Responsible for formatting feeds and creating external reports
    '''
if __name__ == "__main__":
    self.serverconnection = centralServerClient('127.0.0.1','25436')
    
    self.packethistory = []

    def __init__(self,params):
        '''
        Constructor
        '''
    
    def Loop (self):
        '''
        the client loop that allows the interface to keep running
        '''
        self.loop = True
        
        while loop:
            #Overview(self.packethistory)
            self.command = input()
            if self.command = 'shutdown':
                pass
            elif self.command = 'show_all_packets':
                Overview(self.packethistory)
            elif self.command = 'show_incoming_packets':
                self.serverconnection.
                Overview()
            elif self.command = 'help':
                print("shutdown"+"\n"+"show_all_packets"+"/n"+"show_incoming_packets"+"/n"+"connect")
            elif self.command = 'connect':
                ip = input('IP? ')
                port = input('Port? (default mainport = 25436)')
                self.serverconnection.connect(ip,port)
                
                self.loop = False
                
    def Overview(self,*datapackets):
        for data in datapackets:
            print("Version: "+datapackets.ipVersion+'\n')
            print("Header length: "+datapackets.ipHLength+'\n')
            print("TTL: "+datapackets.ttl+'\n')
            print("Protocol:" +datapackets.protocol+'\n')
            print("Source Address: "+datapackets.sourceAddr+'    '+"Destination Address: "+datapackets.destAddr+'\n')
            print("Source Port: "+datapackets.sourcePort+'    '+"Destination Port: "+datapackets.destPort+'\n')
            print("Sequence Number: "+datapackets.seqNum+'\n')
            print("Ack: " +datapackets.Ack+'\n')