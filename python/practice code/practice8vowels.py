word = input("Enter a word:")
 
vowels = "aeiou"

count = 0

for character in word:
    if character in vowels:
        count=count+1

print(count)