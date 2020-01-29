import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Insert server IP')
si = input()
print('Insert server port')
port = int(input())
sock.connect((si, port))
print('<create> game or <join> game?')
mode = input()
if mode == 'create':
    sock.send(b'create')
    sudata = sock.recv(256).decode()
    if sudata == 'FATAL ERROR':
        print('it seems like your problem')
    else:
        print(sudata, 'Will play with you')
        while 1:
            print('Insert your data')
            data = input()
            sock.send(bytes(data, 'utf-8'))
            if data == 'STOP_CONNECTION':
                sock.close()
            word = sock.recv(256).decode()
            print(word)
else:
    print('What is target?')
    target = input()
    sock.send(target)
    result = sock.recv(256).decode()
    if result == 'FATAL ERROR':
        print('it seems like your problem')
    else:
        while 1:
            print('Insert your data')
            data = input()
            sock.send(bytes(data, 'utf-8'))
            if data == 'STOP_CONNECTION':
                sock.close()
                break
