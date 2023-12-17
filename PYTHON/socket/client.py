import socket 

def client():
    sock = socket.socket()
    host = '127.0.0.1'
    port = 8000
    sock.connect((host,port))
    while(1):
        try:
            x = input('Enter New Message:').encode()
            sock.send(x)
            data = sock.recv(1024).decode()
            print(f'server wrote : {data}')
        except:
            exit()
client()