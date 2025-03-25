'''
a=[1,6,7,4]

print(a[1])
print(a[3])
print(a[len(a)-1])
print(a[-1])
print(a[-3])

a[1]=8
print(a)
'''
a=[1,6,7,4,10]
#a.remove(4)
#print(a)
#a.pop(2)
#print(a)
a.sort()
print("Second largest no",a[-2])
print("Second smallest no",a[1])












'''
b=[]
b.append(4)
b.append("Sheela")
print(b)
'''

'''
a=[45,32,4,21,80,7,34]
for i in a:
    print(i)
'''

'''
a=[45,32,4,21,80,7,34]
for i in a:
    if i%2==0:
        print(f"Even numbers are {i}")
    else:
        print(f"Odd numbers are {i}")
'''

'''
a=[45,32,4,21,80,7,34]
for i in a:
    if i%2 and i%4==0:
        print(f"Even numbers are {i}")

'''

'''
a = [45, 32, 13,4, 21, 80, 7, 34]
prime = []
for i in a:
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        prime.append(i)

print(prime)

            
'''








        
    





'''
a=['a',5,6,'sujith']
b=a.copy()
print(b)

'''

'''
a=[56,67,34,45,67]
b=[45,778,3423,67,23]
a.extend(b)
print(a)
'''
'''
a=[56,67,34,45,67]
a.reverse()
print(a)
'''
'''
a=[56,67,34,45,67]
b=[]
for i in range(len(a)-1,-1,-1):
    b.append(a[i])
print(b)

'''



    
