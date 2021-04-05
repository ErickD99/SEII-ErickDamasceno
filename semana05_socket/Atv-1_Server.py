import socket
import pickle

HEADERSIZE = 10


porta = int(input('Digite a porta de conexão: '))
nome_do_arquivo_original = input('Digite o nome_do_arquivo_original.txt a ser compartilhado: ')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), porta))
s.listen(5)


while True:
	clientsocket, address = s.accept()
	print(f'Conexão com {address} estabelecida')

	with open(nome_do_arquivo_original, 'rb') as rf:
		f_aux = rf.read()

	msg = pickle.dumps(f_aux)
	msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg

	clientsocket.send(msg)