import socket
import sys


host = str(sys.argv[1])
port = int(sys.argv[2])
filename = input("Enter file: ")
timeout = 3

bytesToSend = str.encode(filename)

serverAddressPort = (host, port)

bufferSize = 1024



# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)



# Send to server using created UDP socket

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)
server_file = msgFromServer[0].strip()
print(server_file)

while True:
    if server_file:
        f = open(filename, 'wb')
        f.write(server_file)
        f.close()
        break
    else:
        print("No data received")
print("Received")
