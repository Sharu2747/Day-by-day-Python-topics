numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]


odd=[]
even=[]


for num in numbers:
    if num%2==0:
        even.append(num)

    else:
        odd.append(num)

print(even)
print(odd)