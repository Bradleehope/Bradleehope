import socket
import sys


host = socket.gethostname()
port = int(sys.argv[1])
bufferSize = 1024
address = (host, port)


# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)



# Bind to address and ip

UDPServerSocket.bind((host, port))


print("UDP server up and listening on port and IP: ", port, host)



# Listen for incoming datagrams

while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]

    client_address = bytesAddressPair[1]

    clientRequest = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(client_address)

    print(clientRequest)
    print(clientIP)
    if message:
        file_name = message.strip()
    data = "Hello client"
    UDPServerSocket.sendto(bytes(data, 'utf-8'), client_address)
    try:
        f = open(file_name, "r")
        data = f.read(bufferSize)
        print("sending ...")
        UDPServerSocket.sendto(bytes(data, 'utf-8'), client_address)
    except FileNotFoundError:
        data = b'No file found'
        UDPServerSocket.sendto(data, client_address)
    UDPServerSocket.close()
    f.close()
print("Sent!")
