sentence = "python is easy and python is powerful"

words = sentence.split()

count={}

for word in words:
    if word not in count:
     count[word] = 1
    else:
     count[word] = count[word] + 1
print(count)

