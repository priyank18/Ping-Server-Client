import random,time
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM) 
serverSocket.bind(('', 12000))

while True:
 print "Server is working..."
 rand = random.randint(0, 10)
 
 message, address = serverSocket.recvfrom(1024)
 
 rand2 = random.randint(1,5)/10.0
 time.sleep(rand2)
 
 if rand < 4:
    continue
 serverSocket.sendto(message, address)
