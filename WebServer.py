#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM) #AF_INET indicates we're using IPv4, SOCK_STREAM indicates a TCP connection.

#Prepare a server socket
#Fill in start
serverSocket.bind(('',6789)) #binding our server socket to all interfaces on port 6789.
serverSocket.listen(1) #listening with a backlog of 1, so we only queue one incoming connection.
#Fill in end

while True:
  #Establish the connection
  print('Ready to serve...')
  #Fill in start
  connectionSocket, addr = serverSocket.accept() #communication socket; we're creating a new socket just for this client, with their IP/Port in addr.
  #Fill in end
  
  try:
    #Fill in start 
    message = connectionSocket.recv(1024).decode() #using recv to receive request line/headers from the client, with 1024 bytes of buffer
    #then we use .decode() to conver the bytes received from .recv to a string.
  
    #Fill in end 
    filename = message.split()[1]
    f = open(filename[1:])
    #Fill in start 
    outputdata = 
    #Fill in end
    
    #Send one HTTP header line into socket
    #Fill in start
    
    #Fill in end
    #Send the content of the requested file to the client
    for i in range(0, len(outputdata)):
      connectionSocket.send(outputdata[i].encode())
  connectionSocket.send("\r\n".encode())

  connectionSocket.close()
except IOError:
  #Send response message for file not found
  #Fill in start

  #Fill in end
  #Close client socket
  #Fill in start

  #Fill in end
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
