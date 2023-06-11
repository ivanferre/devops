#/usr/bin/python3
#   echo-client.py

import socket

HOST = "127.0.0.1"  # server's IP address (may work also with hostname)
PORT = 65432        # port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # TODO Catch the errors:
    #   ConnectionRefusedError  server is not running
    #   Connection Timed Out
    s.connect((HOST, PORT))
    s.sendall(b"Hello, World!")
    data = s.recv(1024)

print(f"Received {data!r}")
