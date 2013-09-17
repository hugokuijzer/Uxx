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

    def __init__(self,params):
        '''
        Constructor
        Connect to port 27017
        '''
        client = MongoClient('localhost', 27017)
        db = client['NetworkWatchDatabase']
        collection = db.collection
        
    def __CreateDocument__(self, id, param):
        '''
        A function that transforms the id and param into a document object
        '''
        document = {ids: param}
        return document
        
    def __CreateDocuments__(self, ids, params):
        '''
        A function that transforms the ids and params into a document object
        '''
        index = 0
        for param in params:
            documents.append({ids[index]: param})
            index += 1
            
        return documents
        
    def __Get__(self):
        '''
        Getter function that should return the data
        '''
        answer = []
        for posts in collection.find():
            answer.append(posts)
            
        return answer
            
    def __Get__(self,document):
        '''
        Getter function that allows for more then one find
        '''
        answer = []
        for posts in collection.find():
            answer.append(posts)
            
        return answer
        
    def __Get_One__(self,documentorID):
        '''
        Getter function that can get specific data
        '''
        return collection.find_one(documentorID)
        
    def __Set__(self,document):
        '''
        Set function that sends data to the server
        Returns the ID code of the post
        '''
        post = document
        document_id = collection.insert(post)
        return document_id
    
    def __Set__(self,document):
        '''
        Bulk set function, to get massive data into the server
        '''
        new_posts = [document,document]
        collection.insert(newposts)