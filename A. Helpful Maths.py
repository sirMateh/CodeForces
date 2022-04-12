def main():
  arr = sorted([int(i) for i in input().split("+")])
  a = ""
  for i in arr:
    a += (f'{i}+')
  print(a[0:-1])
if __name__ == '__main__':
   main()