inp = input("enter the sentence: ")
'inps = inp.strip()'
inpsp = inp.split(" ")
leng = inpsp.__len__()
i = 0
j = 0
while i < leng:
    j = i+1
    while j < leng-1:
        if inpsp[i] == inpsp[j]:
            inpsp.remove(inpsp[i])
        j = j+1
    i = i+1
print(inpsp)