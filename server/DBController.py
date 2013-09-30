'''
Created on 8 sep. 2013

@author: hugo, Samantha
'''

import pymongo
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
        
    def CreateDocument(self, id, param):
        '''
        A function that transforms the id and param into a document object
        '''
        document = {ids: param}
        return document
        
    def CreateDocuments(self, ids, params):
        '''
        A function that transforms the ids and params into a document object
        '''
        for ids,param in params:
            documents.append({ids: param})
            
        return documents
        
    def Get(self):
        '''
        Getter function that should return the data
        '''
        answer = []
        for posts in self.collection.find():
            answer.append(posts)
            
        return answer
            
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
        return collection.find_one(documentorID)
        
    def Set(self,document):
        '''
        Set function that sends data to the server
        Returns the ID code of the post
        '''
        post = document
        document_id = self.collection.insert(post)
        return document_id
    
    def Set(self,document):
        '''
        Bulk set function, to get massive data into the server
        '''
        new_posts = [document,document]
        self.collection.insert(newposts)
        
