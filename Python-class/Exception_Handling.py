'''
Exception Handling:

Exception Handling in python is to handle the runtime errors

Error in Python can be of two types.
    1.Syntax errors
    2.Exceptions.

Exceptions:
    SyntaxError--misspelled keyword, a missing colon
    TypeError--object of the wrong type, such as adding a string to an integer
    IndexError--index is out of range for a list, tuple, or other sequence types
    KeyError--key is not found in a dictionary
    ValueError--value is not found in a dictionary

    '''

'''
Syntax:

try:
    # Some Code.... 

except:
    # optional block
    # Handling of exception (if required)

else:
    # execute if no exception

finally:
    # Some code .....(always executed)

'''

'''
x=5
try:  
    print(y)
except:
    print("An Exception occured!")
'''

'''
try:
  print(var)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
'''

'''
try:
  var = 0
  print(var + "1")
except NameError:
  print("Variable x is not defined")
except TypeError:
  print("Type error")
except:
  print("Something else went wrong")
'''

'''
try:
    x = int(input("Enter a number: "))
    y = 10 / x
    print("The result is:", y)
except ValueError:
    print("You must enter a valid integer.")
'''

'''
try:
    k = 5//0
    print(k)
 
except ZeroDivisionError:
    print("Can't divide by zero")
 
finally:
    print('This is always executed')

'''
'''
try:    
    even_numbers = [2,4,6,8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index Out of Bound.")
'''
    
















