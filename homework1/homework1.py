# File: homework1. py

a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a float, it includes decimals

c = 3j
print(c)
print(type(c)) # 3j represents a complex number (where j is replaced with i)

d = "hello"
print(d)
print(type(d)) # this is a string, a sequence of characters enclosed in quotes

e = [1, 2, 3]
print(e)
print(type(e)) # this is a list, it stores an ordered collection of items (here they are integers)

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, the pairs of data seperated by a colon are associated

g = (1, 2)
print(g)
print(type(g)) # this is a tuple, tuples are like lists but they are immutable

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # this is a list containing strings

i = True
print(i)
print(type(i)) # this is a boolean, it holds the value true or false

j = None
print(j)
print(type(j)) # this is a NoneType, None represents the absence of a value or a null value

k = [True, "blue", 12]
print(k)
print(type(k)) # this is a list

l = str(14)
print(l)
print(type(l)) # this is a string (note 14 is not an integer in this case)

m = 1e4
print(m)
print(type(m)) # thiis is a float (note its using scientifc notation)

# Answer the folowing questions

# question 1: 9 different datatypes

# question 2: List, String, Int, Float, Boolean, Dictionary, Complex, tuple, NoneType

# question 3: b and m; d and l; e, h, k; 

# question 4: Wrapping the 14 with the str() turned it into a sequence of characters (aka a string, not an int)

# question 5: Lets use the set datatype

numbers = set([1, 2, 3, 3, 2, 1])
print(numbers)
print(type(numbers))

#============ 3.2 Booleans ==============

print(10 > 9) # True, 10 is greater than 9

print(10 == 9) # False

print(10 <= 9) # False

print(bool("abc")) # True

print(bool(123)) # True

print(bool(["apple","cherry", "banana"])) # True

print(bool(True)) # True

print(bool(False)) # False

print(bool(0)) # False

print(bool("")) # False

print(bool(" ")) # True

print(bool(())) # False

print(bool([])) # False

print(bool({})) # False

print(bool(True and False)) # False

print(bool(True and True)) # True

print(bool(False and False)) # False

print(bool(True or False)) # True

print(bool(True or True)) # True

print(bool(False or False)) # False

print(bool(not(False))) # True

print(bool(not(False))) # True

print(bool(not(True))) # False

# I don't really understand why certain expressions returned true or false, for instance "" versus " "

# lets create 2 new expressions

print(bool(str(0))) # True
print(bool('')) # False

# I'm actually not sure why



#============ 3.3 Operators ============

print(10 + 5) # 15, + performs addition
print(10 - 5) # 5, - performs subtraction
print(2 * 4) # 8, * performs multiplication 
print(6 / 3) # 2, / performs addition
print(5 % 2) # 1, % gives you the remainder after dividing two numbers
print(3 ** 2) # 9, ** is the exponential operator
print(15 // 2) # 7, // is the floor division operator


print(5 == 2) # False, == is the equality comparison operator
print(10 != 10) # False, != is the not equal comparison operator
print(2 < 5) # True, < the "less than" comparison operator
print(12 > 5) # True, > the "greater than" comparison operator
print(5 <= 6) # True, <= the "less than or equal to" comparison operator
print(1 >= 10) # False, >= the "greater than or equal to" comparison operator



x = 5

x += 5
print(x)

x -= 4
print(x)

x *= 3
print(x)

#========== 3.3.4 Logical Operations ==========

# Questions 1: and is a logicl operator that returns true if both of the conditions are true



print(bool(1 and 0)) # False

print(bool(1 and 1)) # True

#Question 2: or is a logical operator that checks if at least one condition is true

print(bool(1 or 0)) # True

print(bool(0 or 0)) # False

# Questions 3: not is the logical negation operator

print(bool(not(1))) # False
print(bool(not(0))) # True

#Question 1: The difference between / and // is that / does normal division and returns a float, while // does floor division and returns the whole number rounded down
#Question 2: The difference between % and // is that % gives the remainder after division, while // gives the quotient, which is the whole part of the division
#Question 3: To calculate the remainder when dividing two numbers, you would use the % operator
#Question 4: Assignment operators work by updating the value of a variable in place

#=========== 3.4 Strings ===========

my_string = "hello"
print(my_string) # Prints: hello

print(my_string[0]) # Prints: h

print(my_string[1]) # Prints: e

print(my_string[2]) # Prints: l

print(my_string[3]) # Prints: l

print(my_string[4]) # Prints: o

print(my_string[-1]) # Prints: o

print(my_string[0:3]) # Prints: hel

print(my_string[0:5:2]) # Prints: hlo

print(len(my_string)) # Prints: 5

print(my_string + "goodbye") # Prints: hellogoodbye

print(7*my_string) # Prints: hellohellohellohellohellohellohello

#3.4.1 Questions:

# slicing is a way to extract a portion (a "slice") of a string using index positions

# spliced on 8 and 9

name = "Oski"

print("Hello, my name is", name) # Prints: ('Hello, my name is', 'Oski')

name = "Oski"

# print(f'Hello, my name is {name}')

# An f-string (short for formatted string literal) is a way to embed expressions inside string literals in Python.


# cd
# Changes directories. Use it to move from one folder to another
# Example: cd projects

# ls 
# list all the different folders
# Example: ls

# ls-a
# Does the same thing as ls except it list extra folders that are hidden
# Example: ls-a

# mkdir
# This command can be used to make a new folder
# Example: mkdir my_folder

# cat
# cat (short for concatenate) is a command used to read and display file contents, combine multiple files, or create new ones.

# pwd
# pwd stands for print working directory and it will tell you were you are in your files
# Example: pwd

# cd ..
# his command moves you up one folder in the directory tree
# Example: cd ..

# cd .
# this command doesn't move your anywhere in your directory tree
# Example: cd .

# cd ~
# takes you straight to your home directory
# Example: cd ~

# cp
# it lets you duplicate files or directories
# Example: cp file.txt /home/andrew/Documents/

# mv
# this command lets you move files or rename files and directories
# mv [options] source destination

# rm
# rm means remove it deletes files or directories
# Example: rm file.txt

# clear
# wipes the visible terminal output so you get a clean screen
# Example: clear

# grep
# used to search text for patterns


# ls -l