f = open('teste.txt', 'r') #r, r+, a, w
print(f.name)
print(f.mode)

f.close()

#======================================#

with open('teste.txt', 'r') as f:
	f_read = f.read()
	print(f_read)
	f_readlines = f.readlines()
	print(f_readlines)
	f_readline = f.readline()
	print(f_readline)

	for line in f:
		print(line, end='')

	f.seek(0)

	f_read = f.read(100)
	print(f_read)

	tamanho = 10

	f_read = f.read(tamanho)
	print(f.tell())

	while len(f_read) > 0:
		print(f_read, end='')
		f_read = f.read(tamanho)

#======================================#

with open('teste2.txt', 'w') as f:
	f.write('Testando')

#======================================#

with open('teste.txt', 'r') as rf:
	with open('teste_copia.txt', 'w') as wf:
		for line in rf:
			wf.write(line)

#======================================#

with open('teste.jpg', 'rb') as rf:
	with open('teste_copia.jpg', 'wb') as wf:
		for line in rf:
			wf.write(line)

#======================================#

with open('teste.jpg', 'rb') as rf:
	with open('teste_copia.jpg', 'wb') as wf:
		bloco = 4056
		rf_bloco = rf.read(bloco)
		while len(rf_bloco) > 0:
			wf.write(rf_bloco)
			rf_bloco = rf.read(bloco)

#======================================#