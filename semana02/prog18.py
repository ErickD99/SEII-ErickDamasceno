import builtins

x = 'Variável global x'

def teste(m):
	global z
	y = 'Variável local y'
	z = 'Variável local z'
	print(y)
	print(x)
	print(m)

teste('Variável local m')
print(z)

#===========================================#

n = min([5, 1, 4, 2, 3])
print(n)

#===========================================#

def outer():
	x = 'outer_x'
	y = 'outer_y'

	def inner():
		nonlocal y
		x = 'inner_x'
		y = 'inner_y'
		print(x)
		print(y)

	inner()
	print(x)
	print(y)

outer()