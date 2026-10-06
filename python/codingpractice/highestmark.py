marks = {
    "Math": 85,
    "Python": 92,
    "English": 78,
    "Science": 90
}

highest = list(marks.values())[0]

for mark in marks.values():

  if  mark > highest:
     highest = mark

print(highest)

