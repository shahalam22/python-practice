# create a function
def print_5_times():
    counter = 0;
    while counter < 5:
        print('test')
        counter += 1

# call the function
print_5_times()


# create a function
def print_5_times(parameter = 'loop', loop_time = 5):
    counter = 0;
    while counter < loop_time:
        print(counter, parameter)
        counter += 1
    return 'done'

# call the function
ret_value = print_5_times('test', 3)
print(ret_value)


# exercise

def add_numbers(num1, num2):
    print('Sum of the numbers is :', num1 + num2)

add_numbers(5, 6)


# hypotenuse calculator

def hypotenuse_calculator(a = 1, b = 1):
    c = (a**2 + b**2)**0.5
    return c

a = int(input('Enter a height : '))
b = int(input('Enter a width : '))
ans = hypotenuse_calculator(a, b);
print('Hypotenuse is :', round(ans, 2))


# exercise
def shouter(a_str = 'hello', a_num = 5):
    counter = 0
    while counter < a_num:
        print(a_str.upper())
        counter += 1
        if counter == 10:
            print('You are too loud')
            return 'done'
    return 'done'

value = shouter('hello', 5)
print(value)

print(shouter('hello', 15))