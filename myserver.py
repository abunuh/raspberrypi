#!/usr/bin/python3

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1234 

#print('Host = {}'.format(host))

s.bind((host, port))
s.listen(5)

while True:
    conn, addr = s.accept()
    print("Got a request!" )
    #print(conn)
    conn.close()
