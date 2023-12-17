import socket

def server():
    sock = socket.socket()
    host = '127.0.0.1'
    port = 8000
    
    sock.bind((host,port))
    sock.listen(1)
    print('server Stared')
    conn ,add = sock.accept()
    print('client : ',add)
    while(1):
        data = conn.recv(1024).decode()
        if data.lower() == 'end':
            sock.close()
            exit()
        print(f'Client : {data}')
        conn.send(input('Enter data to client : ').encode())    
server()