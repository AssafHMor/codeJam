#!python3
'''Example of a server program'''
import socket

HOST = socket.gethostname() # Get the name of the current server (for example river)
PORT = 5000              # Arbitrary non-privileged port
BUFF_SIZE = 1024
TIME_OUT = 30  # Max time in seconds to wait for message
s = socket.socket()
s.bind((HOST, PORT))
s.listen(0)
print('Waiting for client connections')
conn, addr = s.accept()
print('Connected')
while True:
    conn.settimeout(TIME_OUT)
    try:
        data = conn.recv(BUFF_SIZE).decode('utf-8')
    except socket.timeout:
        reply_msg = bytes('Why aren\'t you responding?!, you are disconnected', 'utf-8')
        conn.sendall(reply_msg)
        conn.close()
        break
    if not data:
        break
    print('Client says:', data)
    reply_msg = bytes('Thank you for saying: ' + data, 'utf-8') # decode str in utf-8
    conn.sendall(reply_msg)
conn.close()
