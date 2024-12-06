string = str(input())
countL, countU = 0, 0 
for l in string:
    if l == l.lower():
        countL += 1
    else:
        countU += 1
print(string.lower() if countL >= countU else string.upper())