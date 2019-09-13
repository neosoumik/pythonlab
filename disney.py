import math as m
num = int(input('enter the number: '))
add = 0
mul = 0
i = 0
while i<=num:
	add=add+i
	i=i+1
mul=m.factorial(num)
print('Add answer: ',add)
print('Mul answer: ',mul)
