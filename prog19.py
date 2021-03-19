li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

s_li = sorted(li)
print('Array ordenado:\t', s_li)

s_li = sorted(li, reverse=True)
print('Array ordenado decrescente:\t', s_li)

#li.sort(reverse=True)

print('Array original:\t', li)

#===========================================#

tupla = (9, 1, 8, 2, 7, 3, 6, 4, 5)

s_tupla = sorted(tupla)
print('Tupla ordenada:\t', s_tupla)

#===========================================#

di = {'nome: ' 'Erick', 'Emprego: ' 'Engenheiro', 'Idade: ' 'None', 'OS: ' 'Windows'}
s_di = sorted(di)

print('Dicionário:\t', s_di)

#===========================================#

li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key=abs)

print(s_li)

#===========================================#


class Empregado():
	"""docstring for Empregados"""
	def __init__(self, nome, idade, salario):
		
		self.nome = nome
		self.idade = idade
		self.salario = salario
	def __repr__(self):
		return '({}, {}, ${})'.format(self.nome, self.idade, self.salario)

from operator import attrgetter

e1 = Empregado('Erick', 21, 8000)
e2 = Empregado('Ma', 35, 5000)
e3 = Empregado('Eike', 26, 2500)

empregados = [e1, e2, e3]

#def e_sort(emp):
#	return emp.nome

s_empregados = sorted(empregados, key=lambda e: e.nome)
#s_empregados = sorted(empregados, key=attrgetter('idade'))
#s_empregados = sorted(empregados, key=e_sort)
print(s_empregados)