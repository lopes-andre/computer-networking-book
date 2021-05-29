''' Write a simple UDP server application that receives
a message from an UDP client and gets a message (uppercase) and
sets it to uppercase and sends back to the client application
'''

from socket import *
import sys

serverPort = 3087  # Defines the port this socket will be listening

# Opens the socket, AF_INET: IPv4 | SOCK_DGRAM: UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assigns the serverPort to the server socket
serverSocket.bind(("", serverPort))

print("Server is ready to serve...")  # Prints the server is running

while True:
    message, clientAddress = serverSocket.recvfrom(
        2048)  # Receives the messagem from the client

    if message.decode() == "exit":  # If the client sends "exit" the socket and program close
        serverSocket.close()
        sys.exit()

    modifiedMessage = message.decode().upper()  # Modifies the message to upper case

    # Sends the modified message to the client
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
