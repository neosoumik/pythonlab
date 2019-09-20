txt = input("enter the string: ")
print("the length of string is ", len(txt), " charecters")
alp = 0
num = 0
space = 0
i = 0
while i < len(txt):
    if txt[i].isalpha():
        alp = alp+1
    if txt[i].isnumeric():
        num = num+1
    if txt[i].isspace():
        space = space+1
    i=i+1
print("the no of alphabets is ", alp)
print("the no of digits is ", num)
print("the no of special chars is ", (len(txt)-alp-num-space))
