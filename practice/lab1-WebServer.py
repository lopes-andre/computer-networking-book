''' In this assignment, you will develop a simple Web server in Python that is capable of
processing only one request. Specifically, your Web server will (i) create a connection
socket when contacted by a client (browser); (ii) receive the HTTP request from this
connection; (iii) parse the request to determine the specific file being requested; (iv) get
the requested file from the server’s file system; (v) create an HTTP response message
consisting of the requested file preceded by header lines; and (vi) send the response
over the TCP connection to the requesting browser. If a browser requests a file that is
not present in your server, your server should return a “404 Not Found” error message. '''

# Import sys and socket module
from socket import *
import sys

# Create a TCP server socket: AF_INET for IPv4 and SOCK_STREAM for TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
serverPort = 80  # Port number
serverSocket.bind(("", serverPort))
serverSocket.listen(1)  # Listening to 1 conection

while True:
    print("Ready to serve...")  # Establish the connection

    connectionSocket, addr = serverSocket.accept()

    # If an exception occurs during the execution of try clause
    # the rest of the clause is skipped
    # If the exception type matches the word after except
    # the except clause is executed
    try:
        message = connectionSocket.recv(1024)
        # Gets the second part of the HTTP header
        filename = message.split()[1]
        f = open(filename[1:])  # Takes off the '\' from the path name
        outputdata = f.read()  # Puts file in a buffer

        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.send("\r\n")

        connectionSocket.close()  # Close the connection socket

    except IOError:
        # Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
        connectionSocket.send(
            "<html><head><title>404 Not Found</title></head><body><center><h1>404 Page Not Found</h1></center></body></html>\r\n")

        # Close client socket
        connectionSocket.close()

serverSocket.close()  # Close server
sys.exit()  # Terminate the program after sending the corresponding data
