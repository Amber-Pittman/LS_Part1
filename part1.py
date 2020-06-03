#print hello world
print("Hello, world!")

# declare a variable
name = "Amber"

#print a variable
print(name)

# String concatenation
print("Hello " + name)

# `Hello ${name}`
print(f'Hello {name}')

# Data Structures

# Array are LISTS in python
p = [10, 25, 60, 8, "Banana"]
print(p)
# add an element to the end of P
p.append(77)
print(p)

# Let's loop over the list P and print every element
# for every element in P, do some sort of code
for element in p:
    print(element)
    #print("this will run after each indexed item")
#print("this will run once because it is outside the for loop")

# Let's print the index and element at the index of P
# p = [10, 25, 60, 8, "Banana"]
# enumerate(p) => [(0, 10), (1, 25), (12, 60) ...]
for (index, element) in enumerate(p): #you can use i or el for these variables
    print(f'Element at {index} is {p[index]}')

# List comprehensions
# another way to create a list
numbers = [1, 4, 9, 16, 25]
# create a new list, of squares, from the numbers list
# Verbose
squares = []
for num in numbers:
  squares.append(numbers)
print(squares)

# Let's use List Comprehensions with elegant code (same as above)
# for each element from numbers, multiply by itself, and add to cooler_squares
# [ function(variable) in some_list]
cooler_squares = [ num*num for num in numbers] # num can be called whatever you want; doesn't matter
print(cooler_squares)

# Let's create a list of just even numbers
even = [num for num in numbers if num % 2 == 0]
print(even)

# create a new list containing only names that start with s
# Also all names should be capitalized
names = ["Sarah", "Jorge", "Sam", "Frank", "bob", "sandy", "shawn"]
# .upper() capitalizes all the letters
# in this situation, .lower() is just checking that the name at 0 is lower
s_names = [name.capitalize() for name in names if name[0].lower() == 's']
print(s_names)

# standard way of naming variables is snake_case, not camelCase

# Dictionaries
# AKA maps/hashmaps/objects
# A key -> value data structure
new_dict = {}

# create a dictionary with ome keys and values
food_dict = {
  "apple": "is a fruit",
  "carrot": "is a veggie"
}
print(food_dict)

# let's add a new key value pair
food_dict['cucumber'] = 'is maybe a veggie?'
print(food_dict)

#access and print a specific element in food_dict
chosen_food = 'apple'
# food_dict.apple is not allowed in python (only JS)
print(food_dict[chosen_food])

# iterate through the keys and values of a dictionary
# for element in dict, do some code
for key, value in food_dict.items():
    print(f'{key} : {value}')

# How can we check if an element exists in a dictionary
# is apple in food_dict?
print('apple' in food_dict) # true
print('banana' in food_dict) # false


# Tuples and Sets

# Tuples
# cannot be changed
tup = (1, 2, 3, 4)
# iterate over tuples
for item in tup:
    print(item)

#access a particular element
print(tup[1])

# you cannot modify tup in any way
#tup[1] = 'new_thing'


# Sets are basically dictionaries without values
# Sets are UNORDERED - if you need them in order, consider using an array
fruit = {'cucumber', 'apple', 'banana'}
fruit_array = ['cucumber', 'apple', 'banana']

for item in fruit:
  print(item)

if 'cucumber' in fruit:
  print("I don't think cucumber is a fruit")

# this is very inefficient
if 'cucumber' in fruit_array:
  print("IDK but please use a set")