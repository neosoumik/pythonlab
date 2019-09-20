import math as m
x=["a","b","c"]
y=[7,5,3]
n=len(x)
m=len(y)
for i in range(n):
    for i in range(m):
        print("{",x[i],"",y[i],"}",end="")
        print("\n")