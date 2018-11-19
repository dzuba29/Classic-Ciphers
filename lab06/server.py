import socketserver
from diffiehellman import *
import json

class Server(socketserver.BaseRequestHandler):
    def start_diffie_hellman(self):
        recv=self.request.recv(1024).decode() #get connection
        print(recv)

        self.privatePrime = RandomPrime()
        self.sharedPrime = RandomPrime()
        self.base = RandomPrime()

        publicSecret=calcKey(self.base,self.privatePrime,self.sharedPrime)

        to_send = {
            'type':'Server',
            'base':self.base,
            'shared_prime':self.sharedPrime,
            'public_secret':publicSecret
        }

        to_send=json.dumps(to_send)
        print(to_send)

        self.request.send(to_send.encode())

        rec_data=self.request.recv(1024)
        rec_data=json.loads(rec_data.decode())

        publicSecret = rec_data['public_secret']

        self.key=calcKey(publicSecret,self.privatePrime,self.sharedPrime)

    def handle(self):
        print("{} my client".format(self.client_address[0]))
        self.start_diffie_hellman()
        print("Secret key{}\n".format(self.key))