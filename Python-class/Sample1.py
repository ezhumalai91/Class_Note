'''
a='mani'
b='bala'
c=a+b
print(c)
'''

'''
n=int(input("Enter any number\t"))
if n%2==0:
    print("Given number is Even")
else:
    print("Given number is Odd")
'''
'''
n=int(input("Enter any number\t"))
if n%2==0 and n%3==0 and n%4==0:
    print("Given number is divisible by 2,3 and 4")
else:
    print("Given number is not divisible by 2,3 and 4")
    
'''
'''
a=input("Enter any character\t")
if a=='d':
    print("Given character is d")
else:
    print("Given character is  not d")
'''

'''
char=input("Enter any character\t")
if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
    print("Given character is Vowel")
else:
    print("Given character is  not Vowel")
'''

'''
a=int(input("Enter A value\t"))
b=int(input("Enter B value\t"))
c=int(input("Enter C value\t"))
d=int(input("Enter D value\t"))
if a>b and a>c and a>d:
    print("A is greater than B,C and D")
elif b>a and b>c and b>d:
    print("B is greater than A,C and D")
elif c>a and c>b and c>d:
    print("C is greater than A,B and D")
else:
    print("D is greater than A,B and C")
'''

'''Looping:'''

'''
for i in range(5):
    print(i)
'''

'''
for i in range(1,5):
    print(i)
'''

'''
for i in range(5,100,5):
    print(i)
'''

'''
tab=int(input("Enter table no\t"))
#count=int(input("Count of the table \t"))
for i in range(1,16):
    print(i," * ",tab," = ",i*tab)
'''

'''
start=int(input("Enter start value"))
end=int(input("Enter end value"))
for i in range(start,end,2):
    print(i)
'''


'''
add=0
n=int(input("Enter any value"))
for i in range(0,n+1,2):
    add=add+i
print("Sum of Natural number is",add)
'''


'''
fact=1
n=int(input("Enter any value"))
for i in range(1,n+1):
    fact=fact*i
print(f"{n}! is",fact)
'''

'''
count=0
n=input("Enter any value")
for i in n:
    count=count+1
print(count)
'''

'''
count=1
n=int(input("Enter any number"))
while count<=n:
    print(count)
    count=count+1
'''

'''
count=1
n=int(input("Enter any number"))
while count<=n:
    print(n)
    n=n-1

'''
'''
count=1
n=int(input("Enter any number"))
print("Odd numbers are")
while count<=n:
    if count%2!=0:
        print(count)
    count=count+1

'''

'''
add=0
count=1
n=int(input("Enter any number"))
while count<=n:
    add=add+count
    count=count+1
print(add)
'''

'''
fact=1
count=1
n=int(input("Enter any number"))
while count<=n:
    fact=fact*count
    count=count+1
print(fact)
'''

'''
# Python while loop exercises to Print Fibonacci Series
a, b = 0, 1
n = int(input("Enter the number of terms: "))
count = 0
while count <= n:
    print(a)
    temp = a + b
    a = b
    b = temp
    count += 1
'''
'''
n = int(input("Enter the number of terms: "))
a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a + b
'''

'''
count=1
n = int(input("Enter the number of terms: "))
a, b = 0, 1
while count<=n:
    print(a)
    a, b = b, a + b
    count+=1
'''




























    






















































