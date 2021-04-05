import socket
import select

HEADERSIZE = 10
PORTA = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((socket.gethostname(), PORTA))
server_socket.listen()

sockets_list = [server_socket]

clients = {}

def receive_msg(client_socket):
	try:
		msg_header = client_socket.recv(HEADERSIZE)

		if not len(msg_header):
			return False

		msg_length = int(msg_header.decode("utf-8").strip())
		return {"header": msg_header, "data": client_socket.recv(msg_length)}

	except:
		return False

while True:
	read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

	for notified_socket in read_sockets:
		if notified_socket == server_socket:
			client_socket, client_adress = server_socket.accept()

			user = receive_msg(client_socket)
			if user is False:
				continue

			sockets_list.append(client_socket)

			clients[client_socket] = user

			print(f"Nova conexao aceita de {client_adress[0]}:{client_adress[1]} usuario:{user['data'].decode('utf-8')}")

		else:
			msg	= receive_msg(notified_socket)

			if msg is False:
				print(f'Conexao fechada de {clients[notified_socket]['data'].decode('utf-8')}')
				sockets_list.remove(notified_socket)
				del clients[notified_socket]
				continue

			user = clients[notified_socket]
			print(f"Mensagem recebida de {user['data'].decode('utf-8')}: {msg['data'].decode('utf-8')}")

			for client_socket in clients:
				if client_socket != notified_socket:
					client_socket.send(user['header'] + user['data'] + msg['header'] + msg['data'])

		for notified_socket in exception_sockets:
			sockets_list.remove(notified_socket)
			del clients[notified_socket]