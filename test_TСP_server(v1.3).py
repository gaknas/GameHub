import socketserver
class TCP_Server(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address)
        mode = self.request.recv(1024).decode()
        if mode == 'create':
            clients[self.client_address] = [True, '']
            print(f'{self.client_adress}: waiting apponent')
            while clients[self.client_address][0]:
                pass
            print(f'{self.client_adress}: apponent appeared')
            while 1:
                self.data = self.request.recv(1024).strip()
                self.data = self.data.decode()
                clients[self.client_address][1] = self.data
                while clients[self.client_address][1] == self.data:
                    pass
                self.request.send(bytes(clients[self.client_address][1]))
                if self.data == 'STOP_CONNECTION':
                    break
                if self.data == 'STOP_SERVER':
                    exit()
        elif mode == 'join':
            
        else:
            self.request.send(b'FATAL ERROR')
clients = {}
if __name__ == "__main__":
    with socketserver.ThreadingTCPServer(('192.168.1.24', 8888), TCP_Server) as server:
        server.serve_forever()
