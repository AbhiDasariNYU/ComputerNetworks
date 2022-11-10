import socket
import os
socket_con=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_con.connect(('10.10.10.2',5000))
f=open("datafile.txt","+w")
print ("enter data") 
for i in range(4):
    f.write(raw_input()+"\n")
f.close()
f=open("datafile.txt" , 'rb') 
l=f.read(1024) 
while(l):
    socket_con.send(l)
    l=f.read(1024)
f.close()
socket_con.shutdown(socket.SHUT_WR) 
socket_con.close()