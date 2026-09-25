numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]

count={}

for num in numbers:
  if num not in count:
        count[num] = 1
  else:
        count[num] = count[num] + 1

print(count)
