'''
Created on 8 sep. 2013

@author: hugo
'''
import queue

class centralController(object):
    '''
Central controller class that links the server request from the user interface to request
made by the filterAgent client and makes sure that all data is properly stored in the database
    '''


    def __init__(self,params):
        '''
        Constructor
        '''
        