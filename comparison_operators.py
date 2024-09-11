# Equal to: True if both operands are equal
print("Equal to: True if both operands are equal")
a = 5
b = 5
c = 9
print(a == b)
print(a == c)
print()

# Not equal to: True if operands are not equal
print("Not equal to: True if operands are not equal")
print(a != b)
print(a != c)
print()

# Greater than: True if the left operand is greater than the right
print("Greater than: True if the left operand is greater than the right")
print(a > b)
print(b > a)
print()

# Less than: True if the left operand is less than the right
print("Less than: True if the left operand is less than the right")
print(a < b)
print(c < a)
print()

# Greater than or equal to: True if left operand is greater than or equal to the right
print("Greater than or equal to: True if left operand is greater than or equal to the right")
print(a >= b)
print(c >= a)
print()

# Less than or equal to: True if left operand is less than or equal to the right
print("Less than or equal to: True if left operand is less than or equal to the right")
print(a <= b)
print(a <= c)
print()

# It Consist of mixture of above Operators. chaining comparison operators
print("chaining comparison operators")
print(1 < a < 10)
print(10 > a <= 9)
print(5 != a > 4)
print(a < 10 < a*10 == 50)
