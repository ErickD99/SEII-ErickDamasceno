print('Módulo importado com sucesso!!!')

def encontra_indice(lista, alvo):
	for i, value in enumerate(lista):
		if value == alvo:
			return 1

	return -1

teste = 'Testado.'