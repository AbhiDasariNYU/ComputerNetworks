import socketserver 
import string 
import os
class FileHandle(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data=self.request.recv(1024).strip()
            print("{}:{} wrote:".format(self.client_address[0],self.client_address[1]))
            data=self.data
            if not data:
                break
            f=open("data.txt", "wb") 
            f.write(data) 
            f.close() 
        os.system("cat data.txt")
s=socketserver.TCPServer(("10.10.10.2",5000),FileHandle)
s.serve_forever()