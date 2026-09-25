numbers = [10, 45, 23, 67, 89, 34, 56]

largest= numbers[0]
second_largest=numbers[0]

for num in numbers:
    if num>largest:
        second_largest=largest
        largest=num

    elif num > second_largest:
      second_largest = num
    

print(largest)
print(second_largest)