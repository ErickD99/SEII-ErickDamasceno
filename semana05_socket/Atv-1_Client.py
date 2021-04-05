import socket
import pickle

HEADERSIZE = 10

porta = input('Digite a porta de conexão: ')
nome_do_arquivo_destino = input('Renomeie e arquivo a ser recebido: ')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), int(porta)))

while True:
	full_msg = b''
	new_msg = True

	while True:
		msg = s.recv(16)

		if new_msg:
			print(f'Comprimento do arquivo: {msg[:HEADERSIZE]}')
			msglen = int(msg[:HEADERSIZE])
			new_msg = False

		full_msg += msg

		if len(full_msg) - HEADERSIZE == msglen:
			print('Arquivo recebido...')

			d = pickle.loads(full_msg[HEADERSIZE:])
			print(d)

			with open(nome_do_arquivo_destino + '.txt', 'wb') as wf:
				wf.write(d)

			new_msg = True
			full_msg = b''

