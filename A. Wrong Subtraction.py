n,k = map(int, input().split(' '))
for i in range(0, k): 
    if str(n)[-1] == '0': 
        n //= 10
    else:
        n -= 1
print(int(n))