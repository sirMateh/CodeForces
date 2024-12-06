s = input().lower() 
vowels = ['a', 'e', 'i', 'o', 'u', 'y'] 
new_str = "" 
for letter in s:
    if letter not in vowels:
        new_str += f".{letter.lower()}" 
print(new_str)