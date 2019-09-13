nu = int(input('enter the number : '))
i = 0
k = 0
n = 0


def fib(a):
    l = 0
    u = 1
    while True:
        if u == a:
            return 1
        if u > a:
            return 0
        temp = u
        u = l+u
        l = temp


if fib(nu) == 1:
    print('it is a part of fibbonaci series')
else:
    print('it is not a part of fibbonaci series')
while i <= nu/2:
    if i*i == nu:
        print('it is a perfect square')
        k = 1
    if 2**i == nu:
        print('it is a perfect power of 2')
        n = 1
    i = i+1


if k == 0:
    print('not a perfect square')
if n == 0:
    print('not a perfect power of 2')
