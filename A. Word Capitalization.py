def main():
   w = str(input())
   if w[0] == w[0].lower():
      print(w[0].upper() + w[len(w)-(len(w)-1):])
   elif w[0] == w[0].upper():
      print(w)
if __name__ == '__main__':
   main()
