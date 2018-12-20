import socket
UDP_IP = "10.160.108.101"
UDP_PORT = 5005
MESSAGE= (b"?")


sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto("cinema".encode(), (UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(1024)
print("Instruction : ", data)
code(data)
data, addr = sock.recvfrom(1024)
print("Instruction : ", data)
