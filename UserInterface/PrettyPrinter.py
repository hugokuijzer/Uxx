'''
Created on 8 sep. 2013

@author: hugo
'''
import UserInterface.centralServerClient as centralServerClient

class prettyPrinter(object):
    '''
    Responsible for formatting feeds and creating external reports
    '''
if __name__ == "__main__":
    
    

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
            self.command = input()
            if self.command = 'shutdown':
                pass
            elif self.command = 'connect':
                ip = input('IP: ')
                port = input('Port: ')
                centralServerClient.connect(ip,port)
                
                self.loop = False