import socket
from diffiehellman import *
import json

class Client:
    def start_diffie_hellman(self,socket):
        socket.send("connected".encode())

        rec_data = socket.recv(1024)
        print(rec_data)

        rec_data=json.loads(rec_data.decode())

        self.privatePrime=RandomPrime(128)
        self.sharedPrime=int(rec_data['shared_prime'])
        self.base=int(rec_data['base'])
        recPublicSecret=int(rec_data['public_secret'])

        senPublicSecret=calcKey(self.base,self.privatePrime,self.sharedPrime)

        to_send = {
            'type':'Client',
            'public_secret':senPublicSecret
        }

        to_send=json.dumps(to_send)
        print(to_send)

        socket.send(to_send.encode())

        self.key=calcKey(recPublicSecret,self.privatePrime,self.sharedPrime)

    def start_client(self,ip):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((ip, 3000))
            self.start_diffie_hellman(sock)
            print("Secret key {}".format(self.key))
        finally:
            sock.close()