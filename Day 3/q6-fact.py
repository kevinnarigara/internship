def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

n = int(input("Enter a number: "))
if n < 0:
    print("You have entered negative number.")
elif n == 0:
    print("Factorial of 0 is 1")
else:
    res = fac(n)
    print("Factorial of {0} is {1}".format(n, res))
