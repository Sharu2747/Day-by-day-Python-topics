sentence = "python is easy and python is powerful"

count={}
words=sentence.split()

for word in words:
    if word not in count:
        count[word]=1
    else:
        count[word]+=1

print(count)
