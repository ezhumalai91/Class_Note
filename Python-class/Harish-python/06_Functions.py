#Function
# Defenition
# It is a set of statements that when called perform a specific task

'''

def fun_name():
    statement'

'''

'''
def gm():
    print("Hello! Goodmorning")
def gn():
    print("Bye! Goodnight")

gm()
gn()
gm()
gn()
gm()
gm()

'''

'''
def gm():
    print("Hello! Goodmorning")
def gn():
    print("Bye! Goodnight")
n=input("Enter any string")
if n=="gm":
    gm()
elif n=='gn':
    gn()
else:
    print("Invalid input")

'''



'''
def add():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum is: ", a + b)
def sub():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Difference is: ", a - b)

print("Simple Calculator Program")
print("1. Addition\n2. Subtraction")
choice = int(input("Enter your choice: "))
if choice == 1:
    add()
elif choice == 2:
    sub()
else:
    print("Invalid choice")

'''

# def add(a,b):
#     print("Sum is: ", a + b)
# def sub(a,b):
#     print("Difference is: ", a - b)

# print("Simple Calculator Program")
# print("1. Addition\n2. Subtraction")
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# choice = int(input("Enter your choice: "))
# if choice == 1:
#     add(b,c)
# elif choice == 2:
#     sub(a,c)
# else:
#     print("Invalid choice")


# H/W

'''
def ispalindrome(n):
    if n==n[::-1]:
        return True
    else:
        return False

n=input("Please enter any word\t")
#print(n[::-1])
if ispalindrome(n):
    print("Its a palindrome")
else:
    print("Its not a palindrome")

'''

'''
H/w
a=[1,2,3,4,5,6,7,8,9,10]
o/p {1:2,3:4,5:6,7:8,9:10}

a=[1,2,3,4,5,6,7,8,9,10]
o/p [1,10,3,8,5,6,7,4,9,2]
'''


'''
def large_finder(l):
    large=l[0]
    for i in l:
        if large<i:     #1<1....1<2...2<3....3<4...4<5..5<55..55<33..55<99..99<5..
            large=i
    return large


l=[1,2,3,4,5,55,33,99,5]

print(f"Largest no is {large_finder(l)}")

'''

# l=[1,2,4,5,55,3,33,99,5]
# l.sort()
# print(l[2])


l=[1,2,4,5,55,3,33,99,5]

mid=(len(l)-1)/2
print(l[int(mid)])