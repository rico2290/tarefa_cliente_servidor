import socket
import timeit, time

class ServerTCP():
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
            print('Aguradando mensagem em TCP... ')
            try:
                conexao, endereco = self.serverOject.accept()
                if conexao:
                    print('servidor conectado por: {} '.format(endereco))
                    self.listaConexao.append(endereco[1])


            except:
                print('Nenhuma conexao ativa')
            while True:
                dado = conexao.recv(2048)
                if dado == b'CLOSE':
                    #print('Fechando a comunicacao...')  
                    time.sleep(3)  
                    conexao.close()
                    
                if dado == b'UPTIME':
                    print( 'Tempo de execucao: {}'.format(timeit.default_timer() - self.tempo_inicio))
                if dado == b'REQNUM':
                    print('Lista de conexoes: {}'.format(self.listaConexao))
                if dado and dado not in [b'CLOSE', b'UPTIME', b'REQNUM' b'']:
                    print('mensagem: {} do cliente {}'.format(dado, endereco[1]))

                
            conexao.close()

server = ServerTCP('localhost', 4000, 2)
server.enviar_e_receber()