#echo client udp
import socket
HOST="192.168.0.236"
PORT=65432
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    d1=input("Enter your message : ")
    s.sendto(d1.encode("utf-8"),(HOST,PORT))
    data=s.recvfrom(1024)
    print(data[0].decode("utf-8"))
s.close()
