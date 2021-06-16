def main():
   n = int(input())
   if n >= 1 and n <= 150:
      x = 0 
      for p in range(0,n):
         arr = str(input())
         if arr[0] == 'X' or arr[2] == 'X':
               if( arr[1] == '+' and arr[2] == '+') or (arr[0] == '+' and arr[1] == '+'):
                  x += 1
               elif( arr[1] == '-' and arr[2] == '-') or (arr[0] == '-' and arr[1] == '-'):
                     x -= 1 
      print(x)
   elif n <= 0:
      print(0)
if __name__ == '__main__':
   main()