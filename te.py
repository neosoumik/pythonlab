inp = input("enter the sentence: ")
'inps = inp.strip()'
inpsp = inp.split(" ")
inpspp = inpsp
i = 0
for word in inpsp:
    while i < inpspp.__len__():
        if word == inpspp[i]:
            inpspp.remove(word)
        i=i+1
print(inpspp)