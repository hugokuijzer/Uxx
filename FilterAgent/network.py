import socket
import threading
import socketserver
import FilterAgent.ltcp as sniffer
import pickle
from pickle import PickleError

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(4096)
        try:
            pickle.loads(data)
            response = sniffer.sniff(data.protocol);
        except PickleError as err:
            response = err
        except Exception as exc:
            response = exc
        
        
#         cur_thread = threading.current_thread()
#         response = "{}: {}".format(cur_thread.name, data)
        
        self.request.sendall(response)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass
