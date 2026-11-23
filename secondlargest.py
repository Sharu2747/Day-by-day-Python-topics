numbers = [10, 25, 45, 80, 30, 60, 80]

largest=numbers[0]
second_largest=numbers[0]


for num in numbers:
    if num>largest:
        second_largest=largest
        largest=num
    elif num < largest and num > second_largest:
        second_largest=num

print(second_largest)