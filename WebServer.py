#import socket module
from socket import *
import sys # In order to terminate the program
import threading 

def handle_client(connectionSocket): #we need a reusable function to handle multiple clients at once
    try:
        message = connectionSocket.recv(1024).decode() #using recv to receive request line/headers from the client, with 1024 bytes of buffer
        #then we use .decode() to convert the bytes received from .recv to a string

        filename = message.split()[1] #grabs the second element of decoded message;  "/HelloWorld.html"
        f = open(filename[1:]) #open FILENAME in f, removing the initial '/';  "HelloWorld.html"
        outputdata = f.readlines() #since the later for loop iterates by index, we'll want to encode the file as a list of strings

        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode()) #header: "HTTP/1.1 200 OK" is the status line, indicating successful connection
        #"\r\n\r\n" indicates the end of the header, so the next package(s) we send is the body. since this project only has one file, we don't need
        #metadata like file type in the header.
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)): #we're encoding and sending the file line by line
            connectionSocket.send(outputdata[i].encode()) 
        #connectionSocket.send("\r\n".encode()) #optional extra newline at the end of the body; can be removed
        connectionSocket.close() #we done!!

    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode()) 
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode()) #small HTML body so that the browser displays something
        #Close client socket
        connectionSocket.close() #same as above, we done
        # Create a TCP socket using IPv4


#main
serverSocket = socket(AF_INET, SOCK_STREAM) #AF_INET indicates we're using IPv4, SOCK_STREAM indicates a TCP connection.

# Prepare a server socket

serverSocket.bind(('', 6789)) #binding our server socket to all interfaces on port 6789.
serverSocket.listen(5) #listening with a backlog of 5, I won't need any more than 1, but having more backlog capacity is good practice

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #communication socket; we're creating a new socket just for this client, with their IP/Port in addr.

    #spawn a new thread to handle this client
    client_thread = threading.Thread(target=handle_client, args=(connectionSocket,))
    client_thread.start()

#these lines will never run because of the infinite loop, but if I iterate on the lab, who knows
serverSocket.close()
sys.exit() #terminate the program after sending the corresponding data
