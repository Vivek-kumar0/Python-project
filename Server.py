#echo serever udp
import socket
HOST="192.168.0.236"
PORT=65432
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((HOST,PORT))
print("UDP Server is running")
while True:
    data=s.recvfrom(1024)
    message=data[0]
    address=data[1]
    print(message.decode("utf-8"))
    print(format(address))
    s.sendto(message,address)
    
