marks = {
    "Math": 85,
    "Python": 45,
    "English": 78,
    "Science": 35,
    "Tamil": 90
}

count = 0

for mark in marks.values():
  if mark<50:
    count= count+1


print(count)
