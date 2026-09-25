numbers = [10, 20, 30, 40, 50, 60]

total = 0

for i in range(len(numbers)):
    if i % 2 == 0:
        total = total + numbers[i]

print(total)