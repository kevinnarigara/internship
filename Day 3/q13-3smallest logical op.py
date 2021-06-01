n1= float(input('enter 1st number: '))
n2= float(input("enter 2nd number: "))
n3= float(input("enter 3rd number: "))
if (n1<=n2) and (n1<=n3):
    print(n1,"is smallest number")
elif (n2<=n1) and (n2<=n3):
    print(n2,'is smallest number')
else:
    print(n3,'is smallest number')
