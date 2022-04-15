def matriz():
    l, c, v = [int(i) for i in input().split()]
    m = []
    n = []
    for i in range(0, c): 
        n.append(v)
    for i in range(0, l):
        m.append(n)
    for i in m:
        a = str(i).replace(",", "").replace("[", "").replace("]", "")
        print(a)
matriz()
    
