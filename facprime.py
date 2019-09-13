nu = int(input('enter the number: '))
i=1
k=0
print('the factors are')
while i<=nu:
    if nu%i==0:
        print(i)
        k=k+1
    i=i+1
print('the number of factors are ',k)
if k==2:
    print('the number is a prime number')
else:
    print('the number is not a prime number')
