import math as m
a = float(input('enter a:'))
b = float(input('enter b:'))
c = float(input('enter c:'))
d = b*b-4*a*c
if d>0:
	print('roots are real and distinct\n')
	r1 = (-b+m.sqrt(d))/2*a
	r2 = (-b-m.sqrt(d))/2*a
	print(r1,r2)
elif d==0:
	print('roots are real and equal')
	print(-b/2*a)
else:
	print('roots are imaginary')
	real = b/2*a
	img = m.sqrt(-1*d)
	print(real,'+',img,'i')
	print(real,'-',img,'i')
