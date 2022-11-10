import socketserver 
import string

class Echo (socketserver.BaseRequestHandler):
    def handle(self):
        self.data=self.request.recv (1024).strip()
        print("{}: {} wrote:".format(self.client_address[0],self.client_address[1]))
        c=0 
        d="" 
        string=self.data
        if "SECRET" in string:
            for i in range(len(string)):
                if(string[i].isdigit()):
                    c+=1 
                    d+=str(string[i])
            r="Digits in string are: {} and Digits count is {}".format(d,str(c))
            self.request.sendall(r)
        else:
            self.request.sendall("Secret code was not found in the string")
s=socketserver.TCPServer(("10.10.10.2",5000),Echo) 
s.serve_forever()