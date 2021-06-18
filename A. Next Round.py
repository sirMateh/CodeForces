def main():
	count = 0
	arr = input().split(' ')
	scores = input().split(' ')
	k_th = scores[int(arr[1])-1]
	for score in scores:
		if int(score) >= int(k_th) and int(score) > 0:
			count += 1
	print(count)
if __name__ == '__main__':
	main()

# +1 score if >= k_th
