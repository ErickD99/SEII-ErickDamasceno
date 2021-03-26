import os
from datetime import datetime


print(dir(os))
print(os.getcwd())

os.chdir('C:/Users/e-ric/Desktop/UFU/2020-1/Sistemas Digitais/')
print(os.getcwd())

#os.mkdir('Teste_video_10')
os.makedirs('Teste_video_10/Teste_Sub_Diretorio')

#os.rmdir('Teste_video_10')
#os.removedirs('Teste_video_10/Teste_Sub_Diretorio')

os.rename('Teste_video_10', 'Teste_video_10')

print(os.stat('Teste_video_10'))
print(os.stat('Teste_video_10').st_size)


mod_time = os.stat('Teste_video_10').st_mtime
print(datetime.fromtimestamp(mod_time))

#======================================#

for dirpath, dirnames, filenames in os.walk('C:/Users/e-ric/Desktop/UFU/2018-2'):
	print('Diretório atual: ', dirpath)
	print('Diretórios: ', dirnames)
	print('Arquivos: ', filenames)

#======================================#

file_path = os.path.join('C:/Users/e-ric/Desktop', 'teste.txt')
print(file_path)

#======================================#

print(os.path.basename('tmp/teste.txt'))
print(os.path.dirname('tmp/teste.txt'))
print(os.path.split('tmp/teste.txt'))
print(os.path.exists('tmp/teste.txt'))
print(os.path.isdir('tmp/teste.txt'))
print(os.path.isfile('tmp/teste.txt'))
print(os.path.splitext('tmp/teste.txt'))


#print(os.listdir())
