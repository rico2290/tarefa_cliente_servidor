import socket
import timeit, time

class ClienteTCP():
    def __init__(self, localhost, porta):
        self.localhost = localhost
        self.porta = porta
                
    def tempo_execucao(self):
        tempo_fim = timeit.default_timer()
        print('Tempo em execucao: {}'.format((tempo_fim -  self.tempo_inicio)))
    
    def enviar_e_receber(self):
        msm = [b'ola servidor', b'oi mundo', b'UPTIME', b'REQNUM', b'CLOSE']
        try:
            self.sockCliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.sockCliente.connect((self.localhost, self.porta))
            #self.sockCliente.listen(self.num_conexao)
            for m in msm:
                #print(m)
                time.sleep(3)   
                if m == b'CLOSE':
                    self.sockCliente.send(m)
                    print('Fechando a comunicacao do lado do cliente...')  
                    time.sleep(3)                
                    self.sockCliente.close()
                    
                else:
                    self.sockCliente.send(m)
                # dado, servidor = self.sockCliente.recv(2048)
                # print('cliente recebeu: {} do {}'.format(dado, servidor))

        except socket.error as s:
            print(s)
        
server = ClienteTCP('localhost', 4000)
server.enviar_e_receber()