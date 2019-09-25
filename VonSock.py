import socket
import threading
import json
from time import sleep
from datetime import datetime

ConnList = []
NewConnList = []
AddressList = []


class VonSocketServer:

    def CreateSocket(self, address_family, socket_type, host, port, limitNum):
        sock = socket.socket(address_family, socket_type)
        sock.bind((host, port))
        sock.listen(limitNum)
        return sock

    def ListenSocket(self, conn, address):
        while True:
            try:
                data = conn.recv(4096)
                if len(data) > 0:
                    print(address, "-->", data.decode())

                    for x in ConnList:
                        newData = address[0].encode() + " | ".encode() + data
                        x.send(newData)
            except ConnectionResetError as error:
                time = " | " + datetime.now().strftime('%H:%M:%S') + " | "
                exit_message = str(address[0]) + time + " LEFT THE ROOM"
                ConnList.remove(conn)

                if len(ConnList) > 0:
                    for x in ConnList:
                        x.send(exit_message.encode())

                print(error)
                AddressList.remove(address[0])
                a = json.dumps(AddressList)
                for x in ConnList:
                    addressListText = "#331" + a
                    x.send(addressListText.encode())
                    sleep(0.1)
                break

    def ListenConnectionRequests(self, socket, connLimit):
        while True:
            conn, address = socket.accept()
            AddressList.append(address[0])
            ConnList.append(conn)
            NewConnList.append(address)

            if len(ConnList) < connLimit:
                print(ConnList)

                a = json.dumps(AddressList)

                sleep(0.1)

                if address in NewConnList:
                    for x in ConnList:
                        time = " | " + datetime.now().strftime('%H:%M:%S') + " | "
                        infoMessage = str(address[0]) + time + " CONNECTED TO ROOM"
                        addressListText = "#331" + a
                        x.send(addressListText.encode())
                        sleep(0.1)
                        x.send(infoMessage.encode())
                    NewConnList.remove(address)
                threading._start_new_thread(self.ListenSocket, (conn, address))

            else:
                conn.close()
                AddressList.remove(address[0])
                ConnList.remove(conn)


class VonClient:

    def CreateSocket(self, address_family, socket_type):
        SOCK = socket.socket(address_family, socket_type)
        return SOCK

    def ConnectServer(self, SOCK, host, port):
        SOCK.connect((host, port))
        return SOCK

    def SendMessage(self, SOCK, DATA):
        SOCK.send(DATA.encode())

    def ListenServer(self, SOCK):
        while True:
            try:
                data = SOCK.recv(2048)
                print(data.decode())
                return data.decode()
            except ConnectionAbortedError as error:
                break
                print(error)




