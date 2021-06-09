''' Same lab as lab0-UDPClient.py but using a TCP connection
Write a simple TCP Client application that sends
a message to the TCP Server and gets a modified (uppercase) message
from the server and prints on the screen
'''

from socket import *

serverName = "<ADD_HOSTNAME>"  # Add the server's hostname
serverPort = 3125  # Server port number defined on the lab0-TCPServer.py program

# Opens the socket, AF_INET: using IPv4 | SOCK_STREAM: TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Establishes a TCP connection to the server
clientSocket.connect((serverName, serverPort))

# Gets the message to be sent to the server
message = input("Input a lowercase sentence to be modified \'exit\' to close the server): ")

# Sends the encoded message to the Server socket
clientSocket.send(message.encode())

# Receives the modified messagem from the server on the client socket
modifiedMessage = clientSocket.recv(2048)

print(f"\nOriginal message: {message}")
# Prints out the modified (uppercase) message
print(f"\nModified message from the server: {modifiedMessage}")

clientSocket.close()  # Closes the socket
