if True:
	print('Verdadeiro')

if False:
	print('Verdadeiro')

linguagem = 'Python'

if linguagem == 'Python':
	print('É Python')
elif linguagem == 'Java':
	print('É Java')
else:
	print('Não é nenhuma anterior.')

usuario = 'Erick'
logado = True

if usuario == 'ADM' and logado:
	print('Página do ADM.')
else:
	print('Acesso negado.')

if usuario == 'ADM' or logado:
	print('Página do ADM.')
else:
	print('Acesso negado.')

if not logado:
	print('Faça login.')
else:
	print('Bem vindo.')

#======================================#

a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)
print(id(a))
print(id(b))
print(a == b)

#======================================#

condicao = None

if condicao:
	print('Verdadeiro')
else:
	print('Falso')