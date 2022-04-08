def main():
	from math import ceil  
	arr = input().split(' ')
	lst = [int(i) for i in arr if int(i) >= 1]
	arr.clear()
	print(ceil(lst[0]/lst[2]) * ceil(lst[1]/lst[2]))
if __name__ == '__main__':
	main()