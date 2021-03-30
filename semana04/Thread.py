import threading
import concurrent.futures
import time
import requests

'''iniciar = time.perf_counter()

def fazer_algo():
	print('Aguardando 1 segundo...')
	time.sleep(1)
	print('Tempo aguardado...')


fazer_algo()

terminar = time.perf_counter()

print(f'Terminado em {round(terminar-iniciar, 2)}')'''

#====================================#

'''iniciar = time.perf_counter()

def fazer_algo():
	print('Aguardando 1 segundo...')
	time.sleep(1)
	print('Tempo aguardado...')


t1 = threading.Thread(target=fazer_algo)
t2 = threading.Thread(target=fazer_algo)

t1.start()
t2.start()

t1.join()
t2.join()

terminar = time.perf_counter()

print(f'Terminado em {round(terminar-iniciar, 2)}')'''

#====================================#

'''iniciar = time.perf_counter()

def fazer_algo(seconds):
	print(f'Aguardando {seconds} segundos...')
	time.sleep(seconds)
	print('Tempo aguardado...')

threads = []

for _ in range(10):
	t = threading.Thread(target=fazer_algo, args=[5])
	t.start()
	threads.append(t)

for thread in threads:
	thread.join()

terminar = time.perf_counter()

print(f'Terminado em {round(terminar-iniciar, 2)}')'''

#====================================#

iniciar = time.perf_counter() 

def fazer_algo(seconds):
	print(f'Aguardando {seconds} segundos...')
	time.sleep(seconds)
	return f'Tempo aguardado...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:
	secs = [5, 4, 3, 2, 1]
	results = [executor.submit(fazer_algo, sec) for sec in secs]

	for f in concurrent.futures.as_completed(results):
		print(f.result())

	'''results = executor.map(fazer_algo, secs)

	for result in results:
		print(result)'''

terminar = time.perf_counter()

print(f'Terminado em {round(terminar-iniciar, 2)}')

#====================================#

'''img_urls =  ['https://images.unsplash.com/photo-1604605152447-1fcea1a333f3'] #Lista de url das imagens a serem baixadas

t1 = time.perf_counter() #Dispara o 'cronômetro'

def baixar_imagens(img_url):
	img_bytes = requests.get(img_url).content #Faz o request da imagem por meio da url passada por parâmetro e salva seu conteúdo
	img_name = img_url.split('/'[3]) #Corta a url no terceiro caracter '/' para utilizar como nome da imagem
	img_name = f'{img_name}.jpg'
	with open(img_name, 'wb') as img_file: #Abre ou cria um arquivo para leitura e gravação de bytes
		img_file.write(img_bytes) #Escreve os bytes salvos anteriormente
		print(f'{img_name} baixada...')


t1 = time.perf_counter() #Para o 'cronômetro'
print(f'Terminado em {round(t2-t1, 2)}')''' #Mostra na tela quanto tempo durou a aplicação