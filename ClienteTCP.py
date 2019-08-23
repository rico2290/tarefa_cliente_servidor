import socket, os, sys
import timeit, time

class ClienteTCP():
    def __init__(self, localhost, porta):
        self.localhost = localhost
        self.porta = porta
                
    # def tempo_execucao(self):
    #     tempo_fim = timeit.default_timer()
    #     print('Tempo em execucao: {}'.format((tempo_fim -  self.tempo_inicio)))
    
    def enviar_e_receber(self):

        try:
            self.sockCliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.sockCliente.connect((self.localhost, self.porta))
            conexao = True
            while conexao:
                msm = input('Digite a mensagem: ')
                msm = bytes(msm, 'utf-8')
                #self.sockCliente.listen(self.num_conexao)
                time.sleep(1)   
                if msm in [b'CLOSE', b'close']:
                    self.sockCliente.send(msm)
                    print('Fechando comunicacao do lado do cliente...') 
                    conexao= False 
                    time.sleep(2)
                    os.system('cls')                
                    self.sockCliente.close()
                    sys.exit()
                    
                else:
                    self.sockCliente.send(msm)
 

        except socket.error as s:
            print(s)
        
server = ClienteTCP('localhost', 4000)
server.enviar_e_receber()