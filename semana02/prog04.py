cursos = ['Cálculo I', 'Sistemas Embarcados II', 'Mecânica dos Sólidos']
cursos_2 = ['Geometria Analítica', 'Física I']

print(cursos)
print(len(cursos))
print(cursos[2])
print(cursos[-2])
print(cursos[0:2])

cursos.append('Cálculo II')
cursos.insert(2, 'Estatística')
cursos.extend(cursos_2)
cursos.remove('Sistemas Embarcados II')
cursos.pop()
cursos.reverse()
cursos.sort()

nums = [4, 9, 2, 0, 1]

nums.sort(reverse=True)
print(nums)

cursos_ordenados = sorted(cursos)
print(cursos_ordenados)

print(min(nums))
print(max(nums))
print(sum(nums))

print(cursos.index('Cálculo II'))
print('Eletrônica' in cursos)

for curso in cursos:
	print(curso)

for index, curso in enumerate(cursos, start=1):
	print(index, curso)

cursos_str = ', '.join(cursos)
print(cursos_str)

lista = cursos_str.split(', ')
print(lista)

#=====================================================#

list_1 = ['História', 'Matemática', 'Física', 'Computação']
list_2 = list_1

print(list_1)
print(list_2)

# list_1[0] = 'Art'

# print(list_1)
# print(list_2)


# Immutable
# tuple_1 = ('História', 'Matemática', 'Física', 'Computação')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Art'

# print(tuple_1)
# print(tuple_2)

#=====================================================#

cs_courses = {'História', 'Matemática', 'Física', 'Computação'}

print(cs_courses)

set_cursos_1 = {'História', 'Matemática', 'Física', 'Computação'}
set_cursos_2 = {'História', 'Matemática', 'Artes', 'Computação'}

print(set_cursos_1.intersection(set_cursos_2))
print(set_cursos_1.difference(set_cursos_2))
print(set_cursos_1.union(set_cursos_2))

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()