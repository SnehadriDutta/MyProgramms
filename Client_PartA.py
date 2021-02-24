import socket
import datetime
import time



c = socket.socket()

c.connect(('localhost',9999))

input_client = input('Enter the string ')

c.send(bytes(input_client,'utf-8'))


n = c.recv(1024).decode()

if n=='E':
    print("\nEMPTY")
else:
    z = int(n)

    for i in range(z):
        now = datetime.datetime.now()
        print(now.strftime("%d-%m-%Y %H:%M:%S"))
        time.sleep(1)


















































