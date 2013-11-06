import socket
import threading
import socketserver
import json

#custom modules
import FilterAgent.network
import interfaceServer.ThreadedTCPRequestHandler as ThreadedTCPRequestHandler
import interfaceServer.interfaceServer as interfaceServer

# from json.encoder import JSONEncoder
    '''
class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        data +=  'on port '+ str(port)                
        data = json.dumps(data).upper()
    
        cur_thread = threading.current_thread()
        response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
        self.request.sendall(response)
    '''
    '''
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    
    def MasterThread(self):
        
        Threaded TCPServer configuration that handles in self fashion:
        -The main thread enters self function. Listening to a specific port for connections
        -When a connection is made, it will ask for (or the client/agent will inform) the type of connection
        -If the type is established. It will assign a new port to self connection. Informing the other which port it is
        -During sending the answer. self thread will create a new thread that handles listening on that port and process the data/requests
        
        self.mainport = 25436
        s = socket.socket (AF_INET,SOCK_STREAM)
        s.setsockopt(1,2,1)
        s.bind("Network Watcher Database Server", mainport) #binding is a tuple
        s.listen(5)
        newport = mainport+1
        while True:
            try:
                c,a=s.accept()
                print("new connection:",a)
            except KeyboardInterrupt:
                print("Shutdown!")
                break
            except:
                print("failure")
                s.close()
            else:
                _type_ = c.recv(1024).decode('utf8').strip()
                s.send(newport)
                if _type_ == 'agent':
                    snifferclient = filterAgentClient.client(c.ip, newport, "new port:" + newport)
                    print('interface received')
                elif _type_ == 'interface':
                    interfaceclient = interfaceServer.client(c.ip, newport, "new port:" + newport)
                    print('agent received')
                newport += 1
    '''
    
def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        print("Sent : {}".format(message))
        sock.sendall(bytes(message, 'ascii'))
        while True:
            ThreadedTCPRequestHandler.handle(self)
            #print("Received: {}".format(response))
    finally:
        sock.close()
    

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused portz
    interfaceserver = interfaceServer()
    self.mainport = 25436
    s = socket.socket (AF_INET,SOCK_STREAM)
    s.setsockopt(1,2,1)
    s.bind("Network Watcher Database Server", mainport) #binding is a tuple
    s.listen(5)
    newport = mainport+1
    snifferclient = []
    interfaceclient = []
    snif = 0
    intf = 0
    while True:
        try:
            c,a=s.accept()
            print("new connection:",a)
        except KeyboardInterrupt:
            print("Shutdown!")
            for client in snifferclient,interfaceclient:
                client.join()
            break
        except:
            print("failure")
            s.close()
        else:
            _type_ = c.recv(1024).decode('utf8').strip()
            s.send(newport)
            if _type_ == 'agent':
                snifferclient[snif] = threading.Thread(target = client, args=(c.ip, newport, newport))
                snifferclient[snif].start()
                snif+=1
                print('interface received')
            elif _type_ == 'interface':
                interfaceclient[intf] = threading.Thread(target = client, args=(c.ip, newport, newport))
                interfaceclient[snif].start()
                inft+=1
                print('agent received')
            newport += 1
    
    '''
    HOST, PORT = "localhost", 0

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)

    client(ip, port, "Hello World 1")
    client(ip, port, "Hello World 2")
    client(ip, port, "Hello World 3")

    client(ip, port, "Hello World 1")
    client(ip, port, "Hello World 2")
    client(ip, port, "Hello World 3")
    
    client(ip, port, "Hello World 1")
    client(ip, port, "Hello World 2")
    client(ip, port, "Hello World 3")
    server.shutdown()
    '''