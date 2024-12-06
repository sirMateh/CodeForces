x, count = int(input()), 0
for p in (5,4,3,2,1):
    count += x//p
    x -= p*(x//p)
print(count)