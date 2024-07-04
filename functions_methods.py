# functions

print(print('a value'))     # None because inner print returns nothing
print(input('ask for a value '))     # prints the input value given by user as input function returns this

# methods -> functions that are attached to objects or datatypes
print('value'.upper())
print('value'.lower())
print('value'.replace('e', '3'))


# new functions

print(abs(-10))     # absolute value
print(max(1, 2, 3, 4, 5))     # maximum value
print(min(1, 2, 3, 4, 5))     # minimum value
print(len('hello'))     # length of string


# exercise
a = int(input('Enter a height : '))
b = int(input('Enter a width : '))
c = (a**2 + b**2)**0.5
print('The hypotenuse of the triangle is : ', round(c, 2))