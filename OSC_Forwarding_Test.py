import sys
from pythonosc.udp_client import SimpleUDPClient

ClientIp = '127.0.0.1' # LOCALHOST
ClientPort = int(sys.argv[1])

client = SimpleUDPClient(ClientIp, ClientPort)  # Create client
client.send_message('/test/address', 'test string')