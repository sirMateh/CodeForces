def main():
	dict = {'a': 1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10,'k':11,'l':12,'m': 13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22,'w':23,'x':24,'y':25,'z':26}
	x = str(input().lower())
	y =  str(input()).lower()
	count_x = 0 
	count_y = 0
	if x == y:
		print(0) 
	elif x != y:
		for c,n in enumerate(x):
			if dict.get(x[c]) > dict.get(y[c]):
				count_x += 1
				break
			elif dict.get(y[c]) > dict.get(x[c]):
				count_y += 1
				break
		if count_x > count_y:
			print(1)
		elif count_y > count_x:
			print(-1)
if __name__ == '__main__':
	main()
