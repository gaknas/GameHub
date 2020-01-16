import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('176.195.163.164', 8888))
#print('введите IP на который отправить')
#target = input()
fl = False
mode = input()
sock.send(bytes(mode, encoding='utf-8'))
if mode == 'join':
    while 1:
        ni = sock.recv(1024).decode()
        print(ni)
        if ni == 'no games':
            break
        print('найден человек!')
        print('будем играть?[y/n]')
        ans = input()
        if ans == 'n':
            break
        if ans == 'y':
            fl = True
            break
        else:
            print('ошибка ввода')
    if fl:
        while 1:
            ninf = input()
            if ninf == 'close':
                exit()
            sock.send(bytes(ninf, encoding='utf-8'))
            inf = sock.recv(1024).decode()
            print(inf)
    else:
        sock.close()
if mode == 'create':
    while 1:
        inf = sock.recv(1024).decode()
        print(inf)
        ninf = input()
        sock.send(bytes(ninf, encoding='utf-8'))
