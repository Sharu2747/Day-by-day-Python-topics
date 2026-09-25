numbers = [4, 7, 2, 7, 9, 2]

seen=[]

for num in numbers:
    if num in seen:
        print(num)
        break

    else:
        seen.append(num)

    