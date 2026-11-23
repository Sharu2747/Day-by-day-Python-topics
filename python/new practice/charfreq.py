text = "programming"

count={}

for char in text:
    if char not in count:
        count[char] = 1
    else:
        count[char] += 1
print(count)

