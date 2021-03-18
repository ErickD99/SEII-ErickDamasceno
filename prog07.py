nums = [1, 2, 3, 4, 5]

for num in nums:
	if num == 3:
		print('Encontrado.')
		break
	print(num)

for num in nums:
	for letra in 'abc':
		print(num, letra)

for i in range(10):
	print(i)

for i in range(1,11):
	print(i)

x = 0

while  x < 10:
	if x == 5:
		break
	print(x)
	x += 1