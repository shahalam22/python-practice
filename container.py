# A tuple cannot change (immutable) while you can change the values of a list.

a_tuple = (1, 2, 3, 'a string')
print(a_tuple)

a_list = [1, 2, 3, 'a string']
print(a_list)
print(len(a_list))
print(a_list[3])

a_list.append('new value')
print(a_list)

# a_tuple.aapend('new value') # error

a_list[4] = 'changed value'
print(a_list)

a_set = {1, 2, 3}
print(a_set)

b_list = [1, 2, 3, 4, 2, 2]
print(b_list)
print(set(b_list))
print(list(set(b_list)))

a_dictionary = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': ['value3', 'value4', 'value5'],
}

print(a_dictionary)


# how to get values from a container
user_list = ['Lisa', 'Bob', 'Alex', 'Anna', 'John']
print(user_list[0])
print(user_list[-1])
print(user_list[0:3])
print(user_list[0:3:2])


# exercise
exercise_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(exercise_list[7:0:-2])