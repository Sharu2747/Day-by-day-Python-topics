numbers = [10, 20, 30, 40, 50, 60, 70]
target = 35

left=0
right=len(numbers)-1
found = False

while left<=right:
 middle = (left+right)//2

 if numbers[middle]==target:
  print("found")
  found = True
  break

 elif numbers[middle]<target:
  left = middle+1

 else:
   right=middle-1

if found ==False:
  print("not found")

   