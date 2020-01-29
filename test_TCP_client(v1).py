import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Insert server IP')
si = input()
print('Insert server port')
port = int(input())
sock.connect((si, port))
while 1:
    print('Insert your data')
    data = input()
    sock.send(bytes(data, 'utf-8'))
    if data == 'STOP_CONNECTION':
    	sock.close()
    	break
