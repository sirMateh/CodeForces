r = []	
lst = []
s = 0
for array in range(0,5):		
	lst.append(input().split(" "))
for a in range(0,5):
	for b in range(0,5):
		if lst[a][b] == "1":
			r.append(a+1), r.append(b+1)
if int(r[0]) > 3:
    s += int(r[0]) - 3
elif int(r[0]) <= 3: 
	s += 3 - int(r[0])
if int(r[1]) > 3:
	s += int(r[1]) - 3
elif int(r[1]) <= 3:
 	s += 3 - int(r[1])
print(s)
