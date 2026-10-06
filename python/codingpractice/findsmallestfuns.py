numbers = [45, 12, 67, 8, 34]



def find_smallest(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest=num

    return smallest

print(find_smallest(numbers))
