"""
n = input("Please Input Any Number : ")
n = int(n)

if n % 2 == 0:
    print(n,"is Even Number.")
else:
    print(n,"is Odd Number.")
"""

"""
n = input("Enter any number : ")
n = int(n)

if n >= 0:
    if n % 2 == 0:
        print(n,"is positive even number.")
    else:
        print(n, "is positive odd number.")
else:
    if n % 2 == 0:
        print(n, "is negative even number.")
    else:
        print(n, "is negative odd number.")
"""

n = input("Enter any number : ")
n = int(n)

if n >= 0 and n % 2 == 0:
    print(n, "is positive and even number.")
elif n >= 0 and n % 2 == 1:
    print(n, "is positive and odd number.")
elif n < 0 and n % 2 == 0:
    print(n, "is negative and even number.")
else:
    print(n, "is negative and odd number.")