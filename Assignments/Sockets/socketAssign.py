from socket import *                        # Importing socket module       

serverSocket = socket(AF_INET, SOCK_STREAM) # Creating a socket
#Prepare a sever socket 
serverPort = 12000                          # Setting the port to 80, for HTML
serverSocket.bind(('', serverPort))         # Binding the socket to the host name and port
serverSocket.listen(1)                      # Starting the socket to listen for clients wanting to connect

while True: 
    #Establish the connection 
    print 'Ready to serve...' 
    connectionSocket, addr = serverSocket.accept()

    try: 
        message = connectionSocket.recv(1024)
        filename = message.split()[1]                  
        f = open(filename[1:])                         
        outputdata = f.readlines()
        #Send one HTTP header line into socket 
        connectionSocket.send('HTTP/1.0 200 OK\r\n\r\n') 
        #Fill in end                 
        #Send the content of the requested file to the client 
        for i in range(0, len(outputdata)):            
             connectionSocket.send(outputdata[i]) 
        connectionSocket.close() 
    except IOError: 
        #Send response message for file not found 
        connectionSocket.send('404 File Not Found')         
        #Fill in end 
        #Close client socket
        connectionSocket.close() 
        #Fill in end 
        serverSocket.close()