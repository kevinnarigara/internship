n1= float(input('enter 1st number: '))
n2= float(input("enter 2nd number: "))
n3= float(input("enter 3rd number: "))
if n1>=n2:
    if n1>=n3:
        print(n1,"is greatest number")
    else:
        print(n3,'is greatest number')

else:
    print(n2,'is greatest number')