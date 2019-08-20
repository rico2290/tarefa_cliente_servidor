import socket
import os, time, timeit

#Criar Servidor UDP 
class ServerUDP():

    def __init__(self, localhost, porta):
        self.localhost = localhost
        self.porta = porta
        self.tempo_inicio = timeit.default_timer()
        self.listaConexo = []
        
    def get_localhost_(self):
        return self.localhost

    def server_data(self):
        return ServerUDP.__dict__

    def get_porta_(self):
        return self.porta

    def get_default_localhost(self):
        try:
            host = socket.gethostname()
            print(socket.gethostbyname(host))
        except:
            print('Impossível pegar nome da máquina e localhost')

    def tempo_execucao(self):
        tempo_fim = timeit.default_timer()
        print('Tempo em execucao: {}'.format((tempo_fim -  self.tempo_inicio)))
    
    def mostrar(self):
        for l in self.listaConexo:
            print(l)
        
    # bind socket para porta 
    def enviar_e_receber(self):
        enderecoDoServidor = (self.localhost, self.porta)
        self.socket_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket_UDP.bind(enderecoDoServidor)

        while True:
            print('Aguradando mensagem... ')
            mensagem, enderecoDoCliente = self.socket_UDP.recvfrom(2048)
            if mensagem:
                print('Recebido {} do cliente {}'.format(mensagem, enderecoDoCliente))
                self.listaConexo.append(enderecoDoCliente[1])
                print('Lista de conexoes: {}'.format(self.listaConexo))
                
                enviar = self.socket_UDP.sendto(mensagem, enderecoDoCliente)
                print('enviado {} para cliente {}'.format(mensagem, enderecoDoCliente))
                
                print( 'Tempo de execucao: {}'.format(timeit.default_timer() - tempo_inicio))
        # def mostrar(self):
        #     for l in self.listaConexo:
        #         print(l)                
        #         # mostrar()
        #     #     # tempo_execucao()
        #     # else:
        #     #     mostrar()
        #     #     time.sleep(3)
        #     #     tempo_execucao()
    

servidor_udp = ServerUDP('localhost', 9210)
servidor_udp.enviar_e_receber()


