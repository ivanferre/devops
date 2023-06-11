#!/usr/bin/python3
# echo-server.py

import socket

HOST = "127.0.0.1"  # localhost - standard loopback interface address
PORT = 65432        # port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen
    print(f"Accepting...")
    conn, addr = s.accept()
    print(f"Accepted!")
    with conn:
        # pass  # Use the socket object without calling s.close().
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
