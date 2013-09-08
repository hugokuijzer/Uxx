'''
Created on 8 sep. 2013

@author: hugo
'''

class userInterfaceServer(object):
    '''
    Server the User interface connects to with requests for info, because feeds can be live 
    all history info request should be handled on a different port. 
    
    Server uses UDP to speed up connection and threading for each incoming request
    '''


    def __init__(self,params):
        '''
        Constructor
        '''
        