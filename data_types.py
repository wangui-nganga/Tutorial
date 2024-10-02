# string data types

# literal assignment
first = "Milly"
last = "Koi"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

#casting a anumber to a string 
decade = str(1980)
print (type(decade))
print (decade)

statement = "I like rock music fro the " +decade + "s."
print(statement)

# Multiple lines
Multiline ='''
Hey, how are you? 

I was just checking in.
                              All good?


'''
print(Multiline)

# Escaping special characters 
sentence = 'I\'m back at work!\t Hey!\n\nwhere\'s this at\\located?'
print(sentence)

#string methods
print(first)
print(first.lower())
print(first.upper())
print(first)
print(Multiline.title())
print(Multiline.replace("good", "ok"))
print(Multiline)


print(len(Multiline))
Multiline += "                                                          "
Multiline = "                                 " + Multiline
print(len(Multiline))
print(len(Multiline.strip()))
print(len(Multiline.lstrip()))
print(len(Multiline.rstrip()))

print("")

# Build a menu
title  = "menu".upper()
print(title.center(20,"="))
print("coffee".ljust(16, ".") + "$1" .rjust(4))
print("muffin".ljust(16, ".") + "$2" .rjust(4))
print("cheesecake".ljust(16, ".") + "$4" .rjust(4))


print("")

# string index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])


# some methods return boolean data
print(first.startswith("M"))
print(first.endswith("y"))



# Boolean data type
myvalue  = True
x = bool(False)
print(type(x))
print (isinstance(myvalue, bool))

# Numeric data types

# integer type
price = 100
best_price = int(80)
print(type(price))
print (isinstance(best_price, int))

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# comples type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))
print(round(gpa, 1))

import math 

print(math.pi)
print(math.sqrt(64))
print(math.ceil (gpa))
print(math.floor(gpa))

# casting string to a number 
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data
#zip_value = int("New York")
