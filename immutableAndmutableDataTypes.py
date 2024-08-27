"""
Immutable Data Types
    - Integers
    - Floats
    - Strings
    - Tuples

Mutable Data Types
    - Lists
    - Dictionaries
    - Sets
"""

print(10)
print(-5)

print(type(10))
print(type(-5))

# Performing math operations with integers
sum_int = 20 + 30
print(sum_int)

# inputNumber
inputNumber  = 5

# printing the memory address of the int variable
print('Before updating, memory address = ',id(inputNumber))

# here we are updating an int object by assigning a new value to it.
# changing the same input number variable by assigning a new value to it.
inputNumber = 10
# printing the memory address of the int variable after updating using the id()
print('After updating, memory address = ',id(inputNumber))