from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
from pythonosc.udp_client import SimpleUDPClient

import sys

DEBUG = False

RECEIVE_PORT = []
FORWARD_PORT = []
FORWARD_IP_LIST = []

CLIENT_INSTANCE_LIST = []

def loadArgs():
    global RECEIVE_PORT, FORWARD_PORT, FORWARD_IP_LIST
    RECEIVE_PORT = int(sys.argv[1])
    FORWARD_PORT = int(sys.argv[2])
    FORWARD_IP_LIST = sys.argv[3:]

def printInfo():
    print('RECEIVE_PORT:', RECEIVE_PORT)
    print('FORWARD_PORT:', FORWARD_PORT)
    print('FORWARD_IP_LIST:', FORWARD_IP_LIST)

def initOSCClients():
    for i, ip in enumerate(FORWARD_IP_LIST):
        CLIENT_INSTANCE_LIST.append(SimpleUDPClient(ip, FORWARD_PORT))

def default_handler(address, *args):
    for client in CLIENT_INSTANCE_LIST:
        client.send_message(address, args)

def startListening():
    LOCAL_HOST = '127.0.0.1'
   
    dispatcher = Dispatcher()
    dispatcher.set_default_handler(default_handler)
    server = BlockingOSCUDPServer((LOCAL_HOST, RECEIVE_PORT), dispatcher)
    server.serve_forever()


# python OSC_Forwading_Server.py 51001 50001 192.168.0.10 192.168.0.20 192.168.0.30 192.168.0.40
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} [Recevie Port] [Forwarding Port] [Forwarding IP] [Forwarding IP] ...\n')
        
    else:        
        loadArgs()
        printInfo()
        initOSCClients()
        startListening()
        
