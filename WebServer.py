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
    filename = message.split()[1] #grabs the second element of decoded message;  "/HelloWorld.html"
    f = open(filename[1:]) #open FILENAME in f, removing the initial '/';  "HelloWorld.html"
    #Fill in start 
    outputdata = f.readlines() #since the later for loop iterates by index, we'll want to encode the file as a list of strings
    #Fill in end
    
    #Send one HTTP header line into socket
    #Fill in start
    connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode()) #header: "HTTP/1.1 200 OK" is the status line, indicating successful connection
    #"\r\n\r\n" indicates the end of the header, so the next package(s) we send is the body. since this project only has one file, we don't need
    #metadata like file type in the header.
    #Fill in end
    
    #Send the content of the requested file to the client
    for i in range(0, len(outputdata)): #we're encoding and sending the file line by line
      connectionSocket.send(outputdata[i].encode()) 
    connectionSocket.send("\r\n".encode()) #it looks to me that this just adds an additional newline at the end of the sent data

    connectionSocket.close() #we done!!
except IOError:
  #Send response message for file not found
  #Fill in start
  connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode()) 
  connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode()) #small HTML body so that the browser displays something
  #Fill in end
  #Close client socket
  #Fill in start
  connectionSocket.close() #same as above, we done
  #Fill in end
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
