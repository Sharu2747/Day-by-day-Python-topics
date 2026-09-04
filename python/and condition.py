age = int(input("Age:"))
has_id = input("ID(TRUE/FALSE):").lower()=="true"

if age>=18 and has_id:
    print("Allowed")
else:
    print ("not allowed" )   