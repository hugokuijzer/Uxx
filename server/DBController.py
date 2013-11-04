'''
Created on 8 sep. 2013

@author: hugo, Samantha
'''

from pymongo import MongoClient
import FilterAgent.ltcp.ltcp as ltcp

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
        document = {'name':'IPdocument','version':ipVersion,'length':ipHLength,'ttl':ttl,'protocol':protocol,'sourceAddr':sourceAddr,'destAddr':destAddr,'sourcePort':sourcePort,'destPort':destPort,'seqNum':seqNum,'Ack':Ack}
        return document
    
    def CreateTCPDocument(self, destinationport, sourceport, flags):
        document = {'name':'TCPdocument','version':ipVersion,'length':ipHLength,'ttl':ttl,'protocol':protocol,'sourceAddr':sourceAddr,'destAddr':destAddr,'sourcePort':sourcePort,'destPort':destPort,'seqNum':seqNum,'Ack':Ack}
        return document
        
    def CreateDNSDocument(self,transactionid,flags,resourcerecordname):
        document = {'name':'DNSdocument','version':ipVersion,'length':ipHLength,'ttl':ttl,'protocol':protocol,'sourceAddr':sourceAddr,'destAddr':destAddr,'sourcePort':sourcePort,'destPort':destPort,'seqNum':seqNum,'Ack':Ack}
        return document
        
    def CreateUPDDocument(self, sourcePort, destPort, length, data):
        document = {'name':'UPDdocument','destination port': destinationport, 'source port':sourceport, 'length': length, 'data':data}
        return document
    
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
            self.documents.append({id: param})
            
#         return documents
        
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
            self.new_posts.append(document)
            
        self.collection.insert(self.newposts)
        
    def ReturnDataPacket(self,documentorID):
        data = self.ecollection.find_one(documentorID)
        datapack = dataPacket(data['version'], data['length'],data['ttl'],data['protocol'],data['sourceAddr'],data['destAddr'],data['sourcePort'],data['destPort'],data['seqNum'],data['Ack'])
        return datapack