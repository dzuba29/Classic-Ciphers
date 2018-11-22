import socketserver
from elgamal import *
import hashlib
import json

class Server(socketserver.BaseRequestHandler):
    def start_elgamal(self):
        recv = self.request.recv(1024).decode() #get connection
        print(recv)

        self.p = RandomPrime(10)
        self.g = RandomSmallNumber(2,15)

        self.x = RandomSmallNumber(2,self.p-1)

        publicSecret = calcKey(self.g,self.x,self.p) # y

        self.k = RandomK(self.p)

        self.r = calcKey(self.g,self.k,self.p)

        self.message = 'Say hello to my little friend'

        int_hash = int(hashlib.sha1(self.message.encode()).hexdigest(),16)

        self.s = calcS(int_hash,self.x,self.r,self.k,self.p)
        print(self.s)
        to_send = {
            'type':'Server',
            'message':self.message,
            'r':self.r,
            's':self.s,
            'p':self.p,
            'g':self.g,
            'public_secret':publicSecret
        }

        to_send = json.dumps(to_send)
        print(to_send)
        self.request.send(to_send.encode()) #send message, r, s  <m,r,s>

    def handle(self):
        self.start_elgamal()
        print("Sending sign: {}\n r: {}\n s: {}\n".format(self.message,self.r,self.s))