import socket
import threading
import socketserver
import lt

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(2048)
        response = ltcp.sniff(data.protocol);
        
#         cur_thread = threading.current_thread()
#         response = "{}: {}".format(cur_thread.name, data)
        
        self.request.sendall(response)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass
