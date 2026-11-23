numbers = [25, 10, 45, 5, 80, 30, 15]

largest=numbers[0]
smallest=numbers[0]

for num in numbers:
    if num > largest:
        largest=num
    elif num < smallest:
        smallest=num

print(largest)
print(smallest)