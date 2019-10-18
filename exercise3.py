import random

# Part A
a,b = map(int, input('Enter 2 numbers separated by space : ').strip().split(" "))
print('Sum = ',(a+b))
print('Sub = ',(a-b))
print('Mul = ',(a*b))
print('Div = ',(a/b))
print('Power = ',(a**b))
print('Quotient = ',(a//b))

#part B

deck = ['Diamonds', 'Clubs', 'Spades', 'Hearts']
print('Before shuffling : ',deck)
random.shuffle(deck)
print('After shuffling : ',deck)
print('Randomly drawinga suit : ',random.choice(deck))
print('Random new deck : ',random.sample(deck,2))


#Part C

a,b = map(int, input("Enter two numbers : ").strip().split(" "))
print("a = ",a," b = ",b)
c = a
a = b
b = a
print("Swapped using temp var..... a = ",a," b = ",b)

print("swapping without temp var")

a,b = b,a

print("Swapped without temp var..... a = ",a," b = ",b)
