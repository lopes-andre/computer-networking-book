''' Write a simple 
'''

from socket import *

serverName = ''
serverPort = 3085 # Server port number defined on the Lab1-WebServer.py program

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))\

