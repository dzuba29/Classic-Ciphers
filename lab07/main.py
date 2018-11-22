from client import *
from server import *
import sys

def start_client():
    client=Client()
    print("Client started...")
    client.start_client("localhost")

def start_server():
    server = socketserver.ThreadingTCPServer(("", 3000),Server)
    print("Server started...")
    server.serve_forever()

def main():
    for arg in sys.argv[1:]:
        if arg=='server':
            start_server()
        if arg=='client':
            start_client()

if __name__ == "__main__":
    main()
