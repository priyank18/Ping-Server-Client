from __future__ import division
import sys
from socket import *
import time

print "\nPinging the server\n" 					

#Setting UDP client socket
clientSocket = socket( AF_INET, SOCK_DGRAM )
clientSocket.settimeout(1)

#Getting Command Line arguments
serverName =sys.argv[1]
PORT = int(sys.argv[2])
NoDatagrams = int(sys.argv[3])
sequence_number = 1
packet=[]

#Loop to send and receive a number of packets (user specified) 
while sequence_number<=NoDatagrams:
   message = "Ping" 					
   start=time.time() 					
   clientSocket.sendto(message,(serverName, PORT))	
   
   try:
     message, address = clientSocket.recvfrom(1024) 	
     elapsed = (time.time()-start) 			
     print message, " " , sequence_number
     print "RTT is: " + str(elapsed) + " seconds\n" 	
     
     packet.append(elapsed)
      
     sequence_number+=1 
     if sequence_number>NoDatagrams:
       break

   except timeout: 	      			
     print message, " ", sequence_number
     print "Request timed out\n"
     sequence_number+=1 				
     if sequence_number>NoDatagrams:   			
       break

# Calculating resposne time between server and client. 
print "Maximum RTT: ", max(packet)
print "Minimum RTT: ", min(packet)
print "Average RTT: ", sum(packet)/len(packet)
print "Percentage of Packet Loss: ", ((NoDatagrams-len(packet))/NoDatagrams)*100
