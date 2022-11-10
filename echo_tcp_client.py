import socket 
import sys

string=''.join(sys.argv[1:])
print("Sent: "+string)
socket_con=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
socket_con.connect(('10.10.10.2',5000)) 
socket_con.sendall(string) 
data=socket_con.recv(1024) 
print("Recieved: ", data) 
socket_con.close