"""
def multiplication_table(n):
    print(n, "x 1 =", n * 1)
    print(n, "x 2 =", n * 2)
    print(n, "x 3 =", n * 3)


multiplication_table(3)
print()
multiplication_table(3+2)

"""


"""
def multiplication_table(n):
    print("{} x {} = {}".format(n, 1, n * 1))
    print("{} x {} = {}".format(n, 2, n * 2))
    print("{} x {} = {}".format(n, 3, n * 3))
    print("{} x {} = {}".format(n, 4, n * 4))
    print("{} x {} = {}".format(n, 5, n * 5))
    print("{} x {} = {}".format(n, 6, n * 6))
    print("{} x {} = {}".format(n, 7, n * 7))
    print("{} x {} = {}".format(n, 8, n * 8))
    print("{} x {} = {}".format(n, 9, n * 9))
    print("{} x {} = {}".format(n, 10, n * 10))


multiplication_table(7)
print()
multiplication_table(7+2)
"""


def multiplication_table(n):
    for i in range(1, 11):
        print("{} x {} = {}".format(n, i, n * i))


multiplication_table(7)
print()
multiplication_table(7+2)
