from VonSock import VonSocketServer
import socket

MySock = VonSocketServer()
sock = MySock.CreateSocket(socket.AF_INET, socket.SOCK_STREAM, "192.168.1.101", 1080, 5)
MySock.ListenConnectionRequests(sock, 5)