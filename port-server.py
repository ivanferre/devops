#!/usr/bin/env python

import socket

IP_ADDRESS = '127.0.0.1'
HOST = "localhost"
PORT = 50000
BUFFER_SIZE = 1024

# https://twin.sh/articles/17/python-how-to-check-if-a-port-is-in-use

# Create a new socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Attempt the connection
if sock.connect_ex((HOST, PORT)) == 0:
    print("SERVER - Port " + str(PORT) + " is open") # Connected successfully
else:
    print("SERVER - Port " + str(PORT) + " is closed") # Failed to connect because port is in use (or bad host)

sock.bind((IP_ADDRESS, PORT))
sock.listen(1)

conn, address = sock.accept()
print( "SERVER - Connection from: " + address[0] + " Port: " + str(address[1]) )

while True:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    datastr = data.decode()
    print( "SERVER - Received data: " + data)
    conn.send("Echo: " + data)
conn.close()
