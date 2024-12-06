t = 0
entrada = input()
lista = [int(num) for num in entrada.split()]
 
for i in range(1, lista[2]+1):
    t += i*lista[0]
print(t-lista[1] if t-lista[1] > 0 else 0)