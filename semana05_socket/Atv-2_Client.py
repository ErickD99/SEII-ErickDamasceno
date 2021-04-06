import socket
import select
import errno

HEADERSIZE = 10
PORTA = 1234

my_username = input("Usuario: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), PORTA))
client_socket.setblocking(False)

username = my_username.encode("utf-8")
username_header = f"{len(username):<{HEADERSIZE}}".encode("utf-8")
client_socket.send(username_header + username)

while True:
	msg = input(f"{my_username} > ")

	if msg:
		msg = msg.encode("utf-8")
		msg_header = f"{len(msg) :< {HEADERSIZE}}".encode("utf-8")
		client_socket.send(msg_header + msg)

	try:
		while True:
			username_header = client_socket.recv(HEADERSIZE)
			if not len(username_header):
				print("Conexão encerrada pelo servidor.")
				sys.exit()

			username_length = int(username_header.decode("utf-8").strip())
			username = client_socket.recv(username_length).decode("utf-8")

			msg_header = client_socket.recv(HEADERSIZE)
			msg_length = int(msg_header.decode("utf-8").strip())
			msg = client_socket.recv(msg_length).decode("utf-8")

			print(f"{username} > {msg}")



	except IOError as e:
		if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
			print('Reading error', str(e))
			sys.exit()
		continue

	except Exception as e:
		print('General error', str(e))
		sys.exit()
	
