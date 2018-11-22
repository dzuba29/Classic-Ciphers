import socket
from elgamal import *
import json
import hashlib

class Client:
    def start_elgamal(self,socket):
        socket.send("connected".encode())

        rec_data = socket.recv(1024)
        print(rec_data)

        rec_data=json.loads(rec_data.decode())

        self.p=int(rec_data['p'])
        self.g=int(rec_data['g'])
        publicSecret=int(rec_data['public_secret'])

        self.r = int(rec_data['r'])
        self.s = int(rec_data['s'])
        self.message = str(rec_data['message'])

        int_hash = int(hashlib.sha1(self.message.encode()).hexdigest(),16)

        self.sign_answer=calcSign(publicSecret,self.r,self.s,self.g,int_hash,self.p)
        
    def start_client(self,ip):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((ip, 3000))
            self.start_elgamal(sock)
            print("Is sign correct?  {} \n".format(self.sign_answer))
        finally:
            sock.close()