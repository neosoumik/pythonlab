txt = ["hello", "hi", "welcome", "oyo", "gmail", "high", "qq"]
count = 0
for x in txt:
    if len(x) >= 2 and x[0] == x[-1]:
        count = count+1
print(count)