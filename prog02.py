message = "Hello World"

print(message)
print(len(message))
print(message[0:11])
print(message.lower())
print(message.upper())
print(message.count('Hello'))
print(message.find('World'))

new_message = message.replace('World', 'Universe')

string_1 = 'Hello'
string_2 = 'World'
message = string_1 + ' ' + string_2
message = '{}, {}!! '.format(string_1, string_2)
message = f'{string_1}, {string_2}!! '

print(dir(string_1))
print(help(str))
