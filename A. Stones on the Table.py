n, c, count = int(input()), str(input()), 0
for i in range(0, n - 1): 
    if c[i+1] == c[i]:
        count += 1
print(count)