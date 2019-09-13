nu = int(input('enter the number : '))
i = 1
nuc = 0
while i<nu:
    if nu%i==0:
        nuc = nuc + i
    i=i+1
if nuc == nu :
    print('number is perfect')
else :
    print('number is not perfect')