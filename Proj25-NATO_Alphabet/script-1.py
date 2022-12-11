# creating new list from a list
# normal way
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(numbers)
print(new_list)

# with list comprehension
new_list1 = [n + 1 for n in numbers]
print(new_list1)

range_list = [n * 2 for n in range(1, 5)]
print(range_list)

# conditional list comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
upper_list = [name.upper() for name in names if len(name) > 5]
print(upper_list)
