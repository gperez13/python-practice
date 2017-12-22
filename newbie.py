# apparently, a hashtag is a comment 
# command question mark does the trick

print('Hello World')

my_message = 'Carry out my wayward son'

print(my_message)

kansas = """There'll be peace when you are done
Lay your weary head to rest
Don't you cry no more"""

print(len(kansas))


greeting = 'Hey'
name = 'Giovanni'

together = '{}, {}. Nice going!'.format(greeting, name)

print(together)



print(4 ** 4)
print(5 * (3 + 9))

num = 2

num *= 10

print(num)

print(abs(-3))

print(round(3.75, 1))


# List, Tuple, & Set time!

fruits = ['banana', 'apple', 'dragonfruit', 'tomato']

print(fruits[2:])

fruits.append('potato')

print(fruits)

fruits.insert(0, 'avocado')

print(fruits)

fruits.remove('potato')

fruits.pop()

print(fruits)

fruits.sort()

print(fruits)


numeros = [2,1,6,9,4,5]

numeros.sort(reverse=True)

print(numeros)


for item in fruits:
	print(item)




touple = ('banana', 'apple', 'dragonfruit', 'tomato')

print(touple)

#sets

fruity = {'banana', 'apple', 'dragonfruit', 'tomato', 'banana'}

print(fruity)






character = {'name': 'Yoshi', 'color': 'green', 'eggs': 'true', 'age': 22}

print(character['name'])



variab = 13

if variab == 17:
	print('true dat')
else: 
	print('nah, fam')





test = [1,2,3,4,5,6,7,8,9]


for num in test:
	if num == 7:
		print('Got em!')
		continue
	print(num)

#break stops the loop iteration





for num in test:
	for letter in 'abc':
		print(num, letter)



for i in range(4, 10):
	print(i)



y = 0

while y < 10:
	if y == 5:
		break
	print(y)
	y += 1






def hello_func(name):
	return 'Hello {}'.format(name)


print(hello_func('Gio'))
# print(len(hello_func()))


# print(hello_func().upper())













