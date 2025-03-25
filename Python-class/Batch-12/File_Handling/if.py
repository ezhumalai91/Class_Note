'''
a=int(input("Enter any number"))
if a%2==0:
    print("Given number is even")
else:
    print("Given number is odd")
'''

a=int(input("Enter any number"))
if a%2==0 and a%3==0 and a%4==0:
    print("Given number is divisible by 2,3,4")
else:
    print("Given number is not divisible by 2,3,4")
