# Rectify the code in each cell


# 1. IndexError
# the list only has 3 elements (indexes 0, 1, 2), so accessing index 6 is out of range
mylist = [14, "hello", 967]
print(mylist[2]) 


# 2. ModuleNotFoundError / ImportError
# pandas and numpy are lowercase — Python module names are case-sensitive
import pandas
import numpy


# 3. SyntaxError
# Print is not a built-in in Python 3, and the string needs to be in parentheses
print("python errors")


# 4. KeyError
# the key True (boolean) is not the same as 'True' (string)
mydictionnary = {True: "hello", False: "bye", '3': "python"}
print(mydictionnary[True]) 


# 5. IndentationError
# the print statement and i+=1 were not indented inside the while block
i = 14
while i < 78:
    print(i)
    i += 1


# 6. StopIteration
# the list only has 3 elements so calling next() a 4th time raises StopIteration
it = iter([1, 2, 3])
next(it)
next(it)
next(it)


# 7. TypeError
# you cannot concatenate a string and an integer directly, need to convert first
print(int('15') + 15) 


# 8. ValueError
# 'python' cannot be converted to an integer, it is not a numeric string
print(int('15')) 


# 9. NameError
# 'python' is not a defined variable anywhere in the code
python_language = "Python"  
print(python_language)


# 10. ZeroDivisionError
# dividing by zero is mathematically undefined and raises an error in Python
x = 19 / 1 
print(x)