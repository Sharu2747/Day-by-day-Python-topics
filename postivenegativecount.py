numbers = [10, -5, 0, 20, -8, 0, 15, -3]

positive=0
negative=0
zeros=0

for num in numbers:
    if num>0:
        positive=positive+1
    elif num<0:
        negative=negative+1
    else:
        zeros=zeros+1

print("Positive numbers:",positive)
print("Negative numbers:",negative)
print("Zeros:",zeros)