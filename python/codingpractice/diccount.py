marks = {
    "Math": 85,
    "Python": 92,
    "English": 48,
    "Science": 67,
    "Tamil": 35
}

count=0

for mark in marks.values():
  if mark >=50:
    count = count+1

print(count)