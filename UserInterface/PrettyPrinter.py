'''
Created on 8 sep. 2013

@author: hugo
'''
import UserInterface.centralServerClient as centralServerClient

class prettyPrinter(object):
    '''
    Responsible for formatting feeds and creating external reports
    '''


    def __init__(self,params):
        '''
        Constructor
        '''
        
    
    def Loop (self):
        '''
        the client loop that allows the interface to keep running
        '''
        loop = True
        
        while loop:
            command = input()
            
            if command = 'shutdown':
                
                loop = False