def  matriz():
    from math import factorial
    l,c =[int(i) for i in input().split()] 
    n = []
    for i in range(0,l):
        n.append("0".split())
        if len(n[i]) < c: 
            for x in range(0,c - len(n[i])):
                n[i].append("0")
    for i in n:
        a = str(i).replace("'", "").replace("[", "").replace("]", "").replace(",", "")
        print(a)
    print(int(factorial((l-1) + (c-1)) / (factorial(l-1) * factorial(c-1) )))
matriz()

    
