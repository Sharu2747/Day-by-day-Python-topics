numbers = [23, 5, 67, 12, 89, 34]

smallest = numbers[0]
largest=numbers[0]

for num in numbers:
    if num<smallest:
        smallest=num
    elif num>largest:
        largest=num

print(smallest)
print(largest)