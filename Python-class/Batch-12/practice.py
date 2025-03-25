#even and odd number
'''a = [1,2,3,4,5,6,7,8]
b=[]
c=[]
for i in a:
    if i%2==0:
        b.append(i)
    elif i%2!=0:
        c.append(i)
print("Even Number:",b)
print("Odd Number :",c)'''

#second largest number
'''list_num = [456, 4, 56, 1000]
print("The list is:",list_num)
list_num.sort()       
print("The second highest number is:",list_num[2]) '''
#largest duplicate number from string

'''a=[1,1,12,2,3,2,3,3,1,1]
b=[]
for i in range (len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
          b.append(a[i])
c=[]        
print("Duplicate number is:",b)
for i in range (len(b)):
    for j in range(i+1,len(b)):
                   if b[i]==b[j]and b[i] not in c:
                      c.append(b[i])
print("largest duplicate number is:",c)
if c:
    highest_duplicate = c[0]
    for i in c:
        if i < highest_duplicate:
            highest_duplicate = i
else:
    highest_duplicate = None
    
print("Duplicate numbers are:", b)

if highest_duplicate is not None:
    print("Highest duplicate number is:", highest_duplicate )
else:
    "No duplicates found"'''

#highest duplicate char
'''s='banannaaa'
a=list(s)
b=[]
for i in range (len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
          b.append(a[i])
c=[]        
print("Duplicate number is:",b)
for i in range (len(b)):
    for j in range(i+1,len(b)):
                   if b[i]==b[j] and b[i] not in c:
                      c.append(b[i])
if c:
    highest_duplicate = c[0]
    for i in c:
        if i < highest_duplicate:
            highest_duplicate = i
else:
    highest_duplicate = None

if highest_duplicate is not None:
    print("Highest duplicate number is:", highest_duplicate )
else:
    "No duplicates found"
'''



'''s='banannaaa'
a=list(s)
b=[]
for i in range (len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
          b.append(a[i])
c=[]        
print("Duplicate number is:",b)
for i in range (len(b)):
    for j in range(i+1,len(b)):
                   if b[i]==b[j] and b[i] not in c:
                      c.append(b[i])
if c:
    highest_duplicate = c[0]
    for i in c:
        if i < highest_duplicate:
            highest_duplicate = i
else:
    highest_duplicate = None

if highest_duplicate is not None:
    print("Highest duplicate number is:", highest_duplicate )
else:
    "No duplicates found"
'''

#to find heighest dupdicate char from split word from string
dic={}
sen='i amaaa boooy. i am comming from ponnnnnndy.'
words=sen.split(' ')
#print(words)
for word in words:
    for i in range(len(word)):
        for j in range(i+1,len(word)):
            if word[i]==word[j]:
                dic[word]={word[i]:word.count(word[i])}  
max_key = max(dic, key=lambda k: max(dic[k].values()))              
print(max_key)



