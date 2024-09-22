#find the largest among 3 numbers entered by the user

a=int(input("Enter The 1st Age:"))
b=int(input("Enter 2nd Age :"))
c=int(input("Enter 3rd Age : "))

if a>b and a>c:
    print("The Greater Number is",a)
elif b>c and b>a:
    print("The Greater Number is",b)
else:
    print("The Greater Number is ",c)