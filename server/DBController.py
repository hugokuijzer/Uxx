'''
Created on 8 sep. 2013

@author: hugo, Samantha
'''

from pymongo import MongoClient

class DBController(object):
    '''
    DBController is the class that interacts with MongoDB to put in data and extract data from the Database
    Functions TODO:
    Set(data)
    Get(data)
    '''

    def init(self,params):
        '''
        Constructor
        Connect to port 27017
        '''
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['NetworkWatchDatabase']
        self.collection = self.db.collection
    
    def CreateIPDocument(self, destination, source, version):
        document = {'destination': destination, 'source': source, 'version':version}
        return document
    
    def CreateTCPDocument(self, destinationport, sourceport, flags):
        document = {'destination port': destinationport, 'source port':sourceport, 'flags': flags}
        return document
        
    def CreateDNSDocument(self,transactionid,flags,resourcerecordname):
        document = {'transaction id': transactionid, 'flags': flags, 'resourcerecordname':resourcerecordname}
    
    def CreateDocument(self, id, param):
        '''
        A function that transforms the id and param into a document object
        '''
        document = {id: param}
        return document
        
    def CreateDocuments(self, ids, params):
        '''
        A function that transforms the ids and params into a document object
        '''
        for id,param in params:
            documents.append({id: param})
            
        return documents
        
    def Get(self,document):
        '''
        Getter function that allows for more then one find
        '''
        answer = []
        for posts in self.collection.find():
            answer.append(posts)
            
        return answer
        
    def Get_One(self,documentorID):
        '''
        Getter function that can get specific data
        '''
        return self.collection.find_one(documentorID)
        
    def Set(self,document):
        '''
        Set function that sends data to the server
        Returns the ID code of the post
        '''
        post = document
        document_id = self.collection.insert(post)
        return document_id
    
    def Set_Documents(self,*documents):
        '''
        Bulk set function, to get massive data into the server
        '''
        for document in documents:
            new_posts.append(document)
            
        self.collection.insert(newposts)
        
