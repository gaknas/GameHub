import socketserver
class TCP_Server(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address)
        while 1:
            self.data = self.request.recv(1024).strip()
            self.data = self.data.decode()
            print(self.data)
            if self.data == 'STOP_CONNECTION':
                break
            if self.data == 'STOP_SERVER':
                exit()
clients = {}
if __name__ == "__main__":
    with socketserver.ThreadingTCPServer(('192.168.1.24', 8888), TCP_Server) as server:
        server.serve_forever()
