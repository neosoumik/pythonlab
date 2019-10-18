# Part A
feet = float(input('Enter feet value : '))
cm = 38.49 * a
print('The value in cm is ',cm,'\n')

#Part B
r = float(input('Enter the radius'))
pi = 22 / 7
area = pi * r ** 2
perimeter = 2 * pi * r

print('area = ',area," perimeter = ", perimeter)

#Part C

a,b,c = map(float, input('Enter the sides a,b and c : ').strip().split(" "))
s = (a+b+c) / 2
area = (s * (s-a) * (s-b) * (s-c)) ** 0.5

print('area of triangle', area)

#Part D

day = int(input("Enter the days : "))
years = int(day/365)
rm = int(day % 365)
weeks = int(rm / 7)
day = rm % 7

print('years = ', years)
print('weeks = ', wweks)
print('days = ', day)
