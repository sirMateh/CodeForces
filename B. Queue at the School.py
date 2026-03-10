n,t = map(int, input().split(' '))
queue, lista = str(input('')), list()

for i in range(0,n):
    lista.append(queue[i])

for i in range(0,t):
    pos = list()
    for x in range(0,n):    
        if x+1 <= n-1  and lista[x] == 'B' and lista[x+1] == 'G' and pos.count(x) == 0:            
            lista[x], lista[x+1] = lista[x+1], lista[x]
            pos.append(x), pos.append(x+1)
queue = ''

for i in lista:
    queue += i

print(queue)




          
            
