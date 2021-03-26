def hello_func():
	print('Hello World!!')

hello_func()


def hello_func_2():
	return 'Hello Universe!!'

print(hello_func_2())
print(hello_func_2().upper())


def hello_fun_3(texto):
	return '{} '.format(texto)

print(hello_fun_3('Olá'))


def hello_fun_3(texto_1, texto_2 = 'Mundo'):
	return '{} {}'.format(texto_1, texto_2)

print(hello_fun_3('Olá', texto_2 = 'Universo'))


def estudante_infos(*args, **kwargs):
	print(args)
	print(kwargs)

estudante_infos('Mecânica', 'Mecatrônica', nome = 'Erick', idade = 21)

cursos = ['Mecânica', 'Mecatrônica']
infos = {'nome': 'Erick', 'idade': 21}

estudante_infos(*cursos, **infos)

#======================================#

n_dias_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def ano_bissexto(ano):
	return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

def dias_no_mes(ano, mes):
	if not 1 <= mes <= 12:
		return 'Mês inválido'
	if mes == 2 and ano_bissexto(ano):
		return 29

	return n_dias_mes[mes]

print(dias_no_mes(2536, 2))