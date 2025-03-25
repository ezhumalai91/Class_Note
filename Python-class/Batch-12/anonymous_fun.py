#Anonymous function

#Lambda Functions
'''
    Lambda Functions are anonymous functions
means that the function is without a name.

Syntax:
     lambda arguments : expression
     
'''

'''
a=lambda x,y: x+y
print(a(4,5))
print(a(40,15)+a(5,4))

'''

'''
#str1 = 'CSC class'
str2=input("Enter any string")
 
upper = lambda string: string.upper()
#print(upper(str1))
print(upper(str2))
'''

'''
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
print(is_even_list)
for item in is_even_list:
    print(item())
'''

'''
Max = lambda a, b : a if(a >b) else b
print("Greater no is:\t",Max(7, 2))
'''


#zip Method:
'''
first=['raja','ravi']
last=['anbu','hema']
a=zip(first,last)

print(list(a))
'''


#Map:---It is a function to which map passes each element of given iterable
'''
Syntax:
    map(funtion, iterable)
'''

'''
def addition(n):
    return n + n

numbers = [1, 2, 3, 4]  #range(1,100)
result = map(addition, numbers)
print(list(result))
'''

'''
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
 
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))
'''

#H/W:check prime  using map

#23---2 to 22----23/2==0

'''
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def print_prime_status(n):
    if is_prime(n):
        return f"{n} is a prime number"
    else:
        return f"{n} is not a prime number"

numbers = range(2, 100)

results = map(print_prime_status, numbers)

print(tuple(results))
'''



'''
#filter fun:
#The filter() method filters the given sequence with the help of a function
    that tests each element in the sequence to be true or not. 

#Syntax: filter(function, sequence)

'''

'''
# a list contains both even and odd numbers. 
seq = [0, 1, 2, 3, 5, 8, 13]
result = filter(lambda x: x % 2 != 0, seq)
print("Odd numbers: ",list(result))
result = filter(lambda x: x % 2 == 0, seq)
print("Even numbers: ",list(result))
'''

'''

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)
print(list(adults))

#for x in adults:
#  print(x)

'''












    
