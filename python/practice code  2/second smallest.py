numbers = [45, 12, 67, 23, 8, 90, 34]

smallest = numbers[0]
second_smallest=numbers[0]

for num in numbers:
    if num<smallest:
        second_smallest=smallest
        smallest=num

    elif  num < second_smallest:
         second_smallest=num


print(smallest)
print(second_smallest)