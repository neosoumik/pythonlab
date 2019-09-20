inp = input("enter the sentence: ")
spinp = inp.split(" ")
for input in spinp:
    print(input[::-1],end=" ")
print()
print(inp[::-1])
i = spinp.__len__() - 1
while i >= 0:
    print(spinp[i],end=" ")
    i=i-1