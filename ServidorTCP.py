import socket
import timeit

class ServidorTCP():
    def __init__(self, localhost, porta, num_conexao:int):
        self.localhost = localhost
        self.porta = porta
        self.num_conexao = num_conexao
        self.listaConexao = []
        self.tempo_inicio = timeit.default_timer()
        
    def tempo_execucao(self):
        tempo_fim = timeit.default_timer()
        print('Tempo em execucao: {}'.format((tempo_fim -  self.tempo_inicio)))
    
    def enviar_e_receber(self):
        self.serverOject = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.serverOject.bind((self.localhost, self.porta))
        #return super().__init__(self.localhost, self.porta,self.num_conexao)
        self.serverOject.listen(self.num_conexao)

        while True:
            print('Aguradando mensagem... ')
            try:
                conexao, endereco = self.serverOject.accept()
                self.listaConexao.append(endereco)
                print('servidor conectado por: {}'.format(endereco))
            except:
                print('Nao deu certo')
            while True:
                dado = conexao.recv(2048)
                if dado == 'CLOSE':
                    break
            conexao.close()

server = ServidorTCP('localhost', 40004, 1)
server.enviar_e_receber()
