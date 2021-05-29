''' Write a simple UDP Client application that sends
a message to the UDP Server and gets a modified (uppercase) message
from the server and prints on the screen
'''

from socket import *

serverName = '<ADD_HOSTNAME>'  # Add the server's hostname
serverPort = 3087  # Server port number defined on the lab0-UDPServer.py program

# Opens the socket, AF_INET: using IPv4 | SOCK_DGRAM: UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Gets the message to be sent to the server
message = input(
    "Input a lowercase sentence to be modified (\'exit\' to close the server): ")

# Sends the encoded message to the Server socket
clientSocket.sendto(message.encode(), (serverName, serverPort))

# Receives the modified messagem from the server on the client socket
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(f"\nOriginal message: {message}")
# Prints out the modified (uppercase) message
print(f"\nModified message from the server: {modifiedMessage}")

clientSocket.close()  # Closes the socket
