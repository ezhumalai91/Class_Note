# Two types of loops:
# 1. for
# 2. while

#loops variables--i,j,k

# print(range(7))
# print(range(3,7))

# for i in range(10):
#     print(i)

# for i in range(10):
#     if i%2==0:
#         print(i)

# for i in range(10):
#     if i%2!=0:
#         print(i)

# for i in range(1,11):
#     # print(i," * 5 = ",i*5)
#     print(f"{i} * 5 = {i*5}")

# for i in range(1,11,3):
#     print(i)



    # O/P
# 1. Anbu
# 2. Lokesh
# 3. Anbu
# 4. Lokesh
# 5. Anbu

# n=int(input("Enter any number"))
# for i in range(n):
#     if i%2==0:
#         print(f"{i}. Anbu")
#     else:
#         print(f"{i}. Lokesh")


    # H/W
# 1. Anbu
# 2. Lokesh
# 3. Harish
# 4. Anbu
# 5. Lokesh
# 6. Harish


#Sequence problem problem
# for i in range(100,1001,100):
#     print(i,end=' ')


#Filtration problem
# a=[1,2,3,4,5,'arthi',6,7,'lokesh',8,9,10,'swathi',True,"Harish",False]

# for i in a:
#     if isinstance(i,int):
#         print(i,end=' ')

'''
#Problem-1: 
# user input 100  to 600
start=int(input("Please enter starting value :"))
end=int(input("Please enter ending value :"))
for i in range(start,end+1):
    print(i)


'''

#Problem-2: sum of n natural no

# 10==1+2+3+----+10==?

# add=0
# n=int(input("Please enter any number:"))
# for i in range(1,n+1):
#     add+=i
# print(add)


#Problem-3: factorial program

# factorial?===5!==5*4*3*2*1

# fact=1
# n=int(input("Please enter any number:"))
# for i in range(1,n+1):
#     fact*=i
# print(fact)


#Problem-4: sum of array

# add=0
# a=[4,7,3,8,9,3,6,7]
# # print(sum(a))
# for i in a:
#     add+=i
# print(add)


'''
#Problem-4: find doublicat

a=[4,7,3,8,9,3,6,7]    #sorting(Selection sort · Bubble sort · Insertion Sort)

a[0]==a[1]
a[0]==a[2]

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            print(a[i])
'''

# While Loop:

# Syntax:

# while condition:
#     body

'''
# sum of n natural using while loop
add=0
count=1
n=int(input("Please enter any number:"))  #10
while count<=n:
    add+=n
    n=n-1
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
