estudante = {'nome': 'Erick', 'idade': 21, 'cursos': ['Mecatrônica', 'SEII']}
estudante['telefone'] = '9 0000 0000'

print(estudante)
print(estudante.get('telefone', 'Não encontrado'))

estudante.update({'nome': 'Mario', 'idade': 5, 'telefone': '0 9999 9999'})
del estudante['idade']
idade = estudante.pop('nome')

print(len(estudante))
print(estudante.keys())
print(estudante.values())
print(estudante.items())

for key, values in estudante.items():
	print(key, values)