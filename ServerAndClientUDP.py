from ServerUDP import*
from ClienteUDP import*
import socket, os


#cliente  = ClienteUDP('localhost', 9890)
server1 = ServerUDP('localhost', 9999)
server2 = ServerUDP('localhost', 9898)
# server3 = ServerUDP('198.160.1.50', 9090, 'localhost')

def cirar_servidor(self):
    ip  = 'localhost'#print(str(input('endereço ip (ex. 192.168.0.1): ')))
    porta  = 8000 #print(str(int('porta (ex. 4444): ')))
    server = ServerUDP(ip, porta)
    return server
    # listaServidor.append(server.server_data())
    
def listar_servidores(self, ServerUDP):
    
    for servidor in self.ServerUDP.:
        if servidor:
            print(servidor)
        else:
            print('lista vazia')
        


def menu():
    print('\t 1 - Criar servidor (informando IP e porta)')
    print('\t 2 - Listar Servidores ativo')
    print('\t 3 - Escolher a qual servidor conectar (informando IP e porta)')
    print('\t 4 - Fechar conexao')
    opcao = print(int(input('selecione uma das opcoes acima: ')))
    
    if opcao == 1:
        cirar_servidor()
        menu()
    if opcao == 2:
        listar_servidores()
#menu()