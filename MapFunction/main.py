import math

# Definition: the map function in Python applies a given function
# to all the items of an iterable (like a list or a tuple) and returns a
# map object (an iteretor). The syntax for the map function is:
# map(function, iterable1, iterable2, ...)

# convert all strings to upper case
words = ["apple", "banana", "cherry"]
uppercase_words = map(str.upper, words)
print(type(uppercase_words))
print("Upper case ---> ", list(uppercase_words))

# square all elements in a list
numbers = [1, 2, 3, 4]
squares = map(lambda x: x**2, numbers)
print("Squares case ---> ", list(squares))

# compute lenght of each word in a list
words = ["python", "java", "C++"]
lenghts = map(len, words)
print("Lenght case ---> ", list(lenghts))


# Concatenate elements for 2 lists
first_names = ["John", "Pippo", "Pluto"]
last_names = ["Smith", "Billy", "White"]
full_names = map(lambda x, y: x + " " + y, first_names, last_names)
print("Concatenate elements case ---> ", list(full_names))

# convert strings to integers
strings = ["1", "2", "3"]
numbers = map(int, strings)
print("Convert to int case ---> ", list(numbers))


# Find the square root of numbers in a list
numbers = [4, 16, 81]
roots = map(math.sqrt, numbers)
print("Square root case ---> ", list(roots))


# Negate all elements in a list
numbers = [5, -4, 3, -2, 1]
negated_numbers = map(lambda x: -x, numbers)
print("Negated number case ---> ", list(negated_numbers))


# Add a constant to all elments in a list
numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x*2, numbers)
print("Constant product * 2 case ---> ", list(result))


# Convert Celsius to Fahrenheit
celsius = [0, 10, 20, 30]
fahrenheit = map(lambda x: (9/5) * x + 32, celsius)
print("Conversion Celsius to Fahrenheit case ---> ", list(fahrenheit))
