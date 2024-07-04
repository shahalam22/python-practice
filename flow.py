# IF condition

if 5 > 4 :
    print('This is true')
else :
    print('This is false')

num = int(input('Enter a number : '))
if num > 0:
    print('The number is positive')
elif num < 0:
    print('The number is negative')
else:
    print('The number is zero')


# while loop

counter = 1
while counter <= 5:
    print('The counter is : ', counter)
    counter += 1
print('The loop is finished')


# for loop

test_list = [1, 2, 3, 4, 5]
for x in test_list:
    print(x)

test_dictionary = {1:'one', 2:'two', 3:'three'}

for key in test_dictionary.keys():
    print(key)

for value in test_dictionary.values():
    print(value)

for key, value in test_dictionary.items():
    print(key, value)


# truthy and falsy values

if 0:                   #try here 0, [], '', None
    print('Truthy')
else:
    print('Falsy')


# exercise

num_list = [1, 2, 3, 4, 5]
for x in num_list:
    if x == 2:
        print('the value is 2')
    else:
        print('the value is not 2')
    
    if x == 5:
        counter = 1;
        while counter <= 6:
            print('last item')
            counter += 1