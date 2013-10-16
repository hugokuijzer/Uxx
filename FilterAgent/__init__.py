import server
from FilterAgent import network
from FilterAgent import ltcp

if __name__ == '__main__':
    network.ThreadedTCPServer.serve_forever()
