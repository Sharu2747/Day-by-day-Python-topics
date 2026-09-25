text = "banana"

count ={}

for character in text:
  if character not in count:
    count[character]=1

  else:
    count[character]=count[character]+1

print(count)