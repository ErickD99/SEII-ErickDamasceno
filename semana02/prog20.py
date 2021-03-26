nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

minha_lista = []

for n in nums:
	minha_lista.append(n)

print(minha_lista)

minha_lista = [n for n in nums]

print(minha_lista)

#===========================================#

minha_lista = []

for n in nums:
	minha_lista.append(n*n)

print(minha_lista)

minha_lista = [n*n for n in nums]

print(minha_lista)

#minha_lista = map(lambda n: n*n, nums)
#print(minha_lista)

#===========================================#

minha_lista = []

for n in nums:
	if n%2 == 0:
		minha_lista.append(n)

print(minha_lista)

minha_lista = [n for n in nums if n%2 == 0]

print(minha_lista)

#minha_lista = filter(lambda n: n%2 == 0, nums)
#print(minha_lista)

#===========================================#

minha_lista = []

for letra in 'abcd':
	for num in range(4):
		minha_lista.append((num, letra))
print(minha_lista)

minha_lista = [(letra, num) for letra in 'abcd' for num in range(4)]
print(minha_lista)

#===========================================#

nomes = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
herois = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

meu_dict = {}

for nome, heroi in zip(nomes, herois):
	meu_dict[nome] = heroi

print(meu_dict)

meu_dict = {nome: heroi for nome, heroi in zip(nomes, herois)}
print(meu_dict)

meu_dict = {nome: heroi for nome, heroi in zip(nomes, herois) if nome != 'Peter'}
print(meu_dict)

#===========================================#

nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
meu_set = set()

for n in nums:
	meu_set.add(n)

print(meu_set)

meu_set = {n for n in nums}

print(meu_set)

#===========================================#

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def gen_func(nums):
	for n in nums:
		yield n*n


meu_gen = gen_func(nums)

for i in meu_gen:
	print(i)

meu_gen = (n*n for n in nums)

for i in meu_gen:
	print(i)

#===========================================#