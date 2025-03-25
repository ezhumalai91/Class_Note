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

#print(range(5))


'''
for i in range(5):
    print(i)
'''

'''
for i in range(5):
    print(i,end='\t')
'''

'''
for i in range(1,5):
    print(i)
'''

'''
for i in range(0,11,2):
    print(i)
'''
'''
for i in range(11,0,-2):
    print(i)
'''

'''
for i in range(5,100,5):
    print(i)
'''

'''
tab=int(input("Enter table no\t"))
count=int(input("Count of the table \t"))
for i in range(1,count+1):
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
for i in range(0,n+1):
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
add=0
a=[4,7,3,8,9,3,6,7]
for i in a:
    add=add+i
print(add)
'''

'''
a=[4,7,3,8,9,3,6,7]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            print(a[i])
'''

'''
veg=[]
for i in range(100):
    ch=input("If you want to add item y-Yes, n-No")
    if ch=='y':
        name=input("Enter product name")
        veg.append(name)
        print("Your product list is : ",veg)
    elif ch=='n':
        exit(0)        
    else:
        print("Invalid choice")
'''        
        
    




    
#While loop:

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
#interchange numbers:
  
a=int(input("Enter the number A:\t"))
b=int(input("Enter the number B:\t"))
temp=a
a=b
b=temp
print(a,"\t",b)
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
#Another method

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

'''
a="Harini"
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            print("Doublicate value is ",a[i])
'''

'''
dup=[]
a="Harini and sheela"
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            dup.append(a[i])
#print(dup)
for i in dup:
    print(i,"count is = ",a.count(i))
'''
#Prime number
n=int(input("Please enter any number:\t"))
for i in range(2,n):
    if n%i==0:
        print(f"{n} is not a prime number")
        break
    else:
        print(f"{n} is a prime number")
        break


























    






















































