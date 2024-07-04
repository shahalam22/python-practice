# f strings
user_name = 'Bob'
user_age = 10

user_information = 'Bob is 10 years old'

bad_approach = user_name + ' is ' + str(user_age) + ' years old.'
print(bad_approach)

good_approach = f'{user_name} is {user_age} years old.'


# single line if statement

user_age = 20
user_status = 'adult' if user_age >= 18 else 'child'
# if user_age < 18:
#     user_status = 'child'
# else:
#     user_status = 'adult'
# print(user_status)

print( f'{user_name} is a {user_age} years old. The person is a {user_status}')


# list comprehension
simple_list = []
for i in range(0,10,1):
    simple_list.append(i)
print(simple_list)

simple_list2 = [i for i in range(0,10,1)]
print(simple_list2)

simple_list2 = [f'{j}{i}' for i in range(0,10,1) for j in ['a','b','c']]
print(simple_list2)

simple_list2 = [f'{j}{i}' for i in range(0,10,1) for j in ('a','b','c') if j == 'a']
print(simple_list2)


# lambda function

def double_value(num):
    return num * 2
print(double_value(2))

double_value = lambda num: num * 2
print(double_value(2))


# some function want a function as an argument
random_list = [5,9,2,4,3,6,8,7]
sorted_list = sorted(random_list)
print(sorted_list)

random_list2 = [('Anna', 25), ('Paul', 18), ('John', 30), ('Mike', 22)]
sorted_list2 = sorted(random_list2, key = lambda x: x[1])
print(sorted_list2)


# exercise
ex_list = [ f'{i}{j}' for i in ['A', 'B', 'C', 'D', 'E'] for j in range(1,6) if f'{i}{j}' != 'C3']
print(ex_list)