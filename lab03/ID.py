a=0
I="A"
D=287414
a=input("Pleas enter a number: ")
x=int(a)
if x%2==0:
    print("This is even")
else:
    print("This is odd")
I=input("Pleas enter your student ID first character: ")
D=input("Pleas enter your student ID last eight number: ")
d=int(D)
if d%2==0:
    print("Your ID number is even")
else:
    print("Your ID number is odd")
print("your student ID is: "+I+D)

