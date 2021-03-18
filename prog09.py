#import modulo_teste as mt
#from modulo_teste import *
from modulo_teste import encontra_indice, teste
import sys
sys.path.append('C:/Users/Erick/Desktop/Modulos')

cursos = ['Mecatrônica', 'Mecânica', 'Estatística', 'Administração']

#print(mt.encontra_indice(cursos, 'Estatística'))
print(encontra_indice(cursos, 'Estatística'))
print(teste)

print(sys.path)

#======================================#

import random

curso_aleatorio = random.choice(cursos)
print(curso_aleatorio)

#======================================#

import math

rads = math.radians(90)
print(rads)

#======================================#

import datetime
import calendar

hoje = datetime.date.today()
print(hoje)

print(calendar.isleap(2020))

#======================================#

import os

print(os.getcwd())
print(os.__file__)

#======================================#

#import antigravity

