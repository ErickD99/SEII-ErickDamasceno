
import multiprocessing
import time
import concurrent.futures
from PIL import Image, ImageFilter

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


p1 = multiprocessing.Process(target='fazer_algo')
p2 = multiprocessing.Process(target='fazer_algo')


p1.start()
p2.start()

terminar = time.perf_counter()

print(f'Terminado em {round(terminar-iniciar, 2)}')'''

#====================================#

'''iniciar = time.perf_counter()

def fazer_algo(seconds):
	print(f'Aguardando {seconds} segundo...')
	time.sleep(seconds)
	print('Tempo aguardado...')

processes = []

for _ in range(10):
	p = multiprocessing.Process(target=fazer_algo, args=[1.5])
	p.start()
	processes.append(p)

for process in processes:
	process.join()

terminar = time.perf_counter()

print(f'Terminado em {round(terminar-iniciar, 2)}')'''

#====================================#

iniciar = time.perf_counter()

def fazer_algo(seconds):
	print(f'Aguardando {seconds} segundos...')
	time.sleep(seconds)
	return f'Tempo aguardado...{seconds}'

with concurrent.futures.ProcessPoolExecutor() as executor:
	secs = [5, 4, 3, 2, 1]
	results = executor.map(fazer_algo, secs)

	for result in results:
		print(result)

terminar = time.perf_counter()

print(f'Terminado em {round(terminar-iniciar, 2)}')

#====================================#

img_names = [] #Array com o nome das imagens a serem processadas

t1 = time.perf_counter() #Dispara o 'cronômetro'

size = (1200, 1200) #Tamanho da imagem em pixels

def process_image(img_name):
	img = Image.open(img_name) #Abre a imagem já existente com o nome passado por parâmetro

	img = img.filter(ImageFilter.GaussianBlur(15)) #Aplica o filtro de interesse

	img.thumbnail(size) #Cria uma miniatura para a imagem
	img.save(f'processada/{img_name}') #Salva a imagem processada
	print(f'{img_name} foi  processada')

with concurrent.futures.ProcessPoolExecuter() as executor:
	executor.map(process_image, img_names) #Utiliza o multiprocessamento para 'mapear' a função process_image com cada uma das imagens do array criado anteriormente

t2 = time.perf_counter() #Para o 'cronômetro'


print(f'Terminado em {t2 - t1} segundos...') #Mostra na tela quanto tempo durou a aplicação