''' Same lab as lab0-UDPClient.py but using a TCP connection
Write a simple TCP server application that receives
a message from a TCP client and gets a message (lowercase) and
sets it to uppercase and sends back to the client application
'''
from socket import *
import sys

serverPort = 3125  # Defines the port this socket will be listening

# Opens the socket, AF_INET: IPv4 | SOCK_STREAM: TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Assigns the serverPort to the server socket
serverSocket.bind("", serverPort)
serverSocket.listen(1)  # Listens to one connection on the "handshake socket"

print("The server is ready to serve...")  # Prints the server is running

while True:
    # Accepts the connection with the client
    connectionSocket, clientAddress = serverSocket.accept()
    # Receives the messagem from the client
    message = connectionSocket.recv(2048)

    # Closes the server if the message is "exit"
    if message.decode() == "exit":
        connectionSocket.close()
        break

    # Modifies the message to upper case
    modifiedMessage = message.decode().upper()

    # Sends the modified message to the client
    connectionSocket.send(modifiedMessage.encode())
    connectionSocket.close()  # Closes the socket

serverSocket.close()  # Closes the handshake socket
sys.exit()
