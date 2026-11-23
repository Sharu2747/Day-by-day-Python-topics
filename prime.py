num = 10
is_prime = True

if num <= 1:
    print("Not prime")
else:

 for i in range(2, num):
    if num % i == 0:
      is_prime = False


 if is_prime==True:
   print("Prime")

 else:
   print("Not prime")

