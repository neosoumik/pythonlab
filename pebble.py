nob = int(input('enter the number of bottles'))
i=1
e=0
o=0
while i<=nob:
    inp = int(input('enter the number of pebbles in'))
    i=i+1
    if inp%2==0:
        e=e+1
    else:
        o=o+1
print('even: ',e)
print('odd: ',o)