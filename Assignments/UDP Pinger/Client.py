# Spencer Davis
# Networks and Data Communications
# 09-28-2018
# UDP Pinger Client

import time
from socket import *

for pings in range(10):

    # Creating the client socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    # Sets the timeout to be one second
    clientSocket.settimeout(1.0)
    # Setting the content of the message
    message = 'test'

    addr = ('127.0.0.1', 12000)

    start = time.time()
    clientSocket.sendto(message, addr)

    try:
        data, server = clientSocket.recvfrom(1024)
        end = time.time()
        timePass = end - start
        print(pings, data, timePass)
    except timeout:
        print("Request timed out.")