import socket
import timeit

class ClienteTCP():
    def __init__(self, localhost, porta):
        self.localhost = localhost
        self.porta = porta
                
    def tempo_execucao(self):
        tempo_fim = timeit.default_timer()
        print('Tempo em execucao: {}'.format((tempo_fim -  self.tempo_inicio)))
    
    def enviar_e_receber(self):
        self.sockCliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sockCliente.connect((self.localhost, self.porta))
        #self.sockCliente.listen(self.num_conexao)
        msm = [b'ola servidor', b'oi mundo', b'kuma ku bu sta']
        for m in msm:
            dado, servidor = self.sockCliente.recv(2048)
            print('cliente recebeu: {} do {}'.format(dado, servidor))
        self.sockCliente.close()

server = ClienteTCP('localhost', 40004)
server.enviar_e_receber()