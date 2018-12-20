import socket
UDP_IP = "10.160.108.101"
UDP_PORT = 5005
MESSAGE= (b"?")


sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto("cinema".encode(), (UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print("received message : ", data)
    
    #sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    #print ("send message :")
    #MESSAGE2= str(input())
    #sock.sendto(MESSAGE2.encode(), (addr))
