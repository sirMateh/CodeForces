a,b = map(int, input().split(' '))
count = 0
while a < b:
        a,b, count = a*3,b*2, count +1 
print(count+1 if a == b else count)