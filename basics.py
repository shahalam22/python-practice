# Execution order

print('line 1')     # 1
print('line 2')     # 2
print('line 3')     # 3


# data types

print('words')
print("words")
print(123)
print(-10)
print(1.5)


# operations

print(1 + 2)
print(1 - 2)
print(1 * 2)
print(1 / 2)
print(1 % 2)
print(10 + 0.123412341234)
# print(10 + 'hello') # error
print(10 * 'hello ') # this will print string 10 times
print(13 - 3 * 4 + 2)   # multiply then add and subtract
print((13 - 3) * (4 + 2))   # first scope add and sub then multiply


# variables

test = 123
print(test)
print(test + 10)

test = test + 100
print(test)


# input

user_input = input("Please write something : ")
print(user_input)

user_name = input("Please write your name : ")
print("Hello " + user_name + ", have a nice day!")
print("Hello", user_name, ", have a nice day!")