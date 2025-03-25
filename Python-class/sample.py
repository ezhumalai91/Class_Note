#for i in range(10):
    #print(i)

#for i in range(3,10):
#    print(i)

#for i in range(2,15,2):
#    print(i)
'''
for i in range(1,16):
   print(i," * ",7," = ",i*7)

for i in range(0,16):
    print(i+1," * ",7," = ",(i+1)*7)
'''
'''
a=[4,6,46,54,34,8,3,56]
print(min(a))
print(max(a))
print(sum(a))
for i in a:
    print(i)
'''

'''
a=[4,6,46,54,34,8,3,56]
b=[]
for i in a:
    b.append(i)
print(b)
'''

'''
dict={}
count=1
n=int(input("Please enter how many student need to be add in database"))
while count<=n:#1<=5
    name=input(f"Enter student Name_{count}")
    dict[f"Student_{count}"]=name
    count=count+1
print(dict)
'''

'''
dict={"A":45,"B":56,"C":67,"Z":43}
for i in dict:
    print(i)
    print(dict[i])
'''
'''
dict={"A":45,"B":56,"C":67,"Z":44}
for i in dict:
    if dict[i]%2==0:
        print(dict[i])
'''

'''
s=input("Please enter any string")
if 'a' in s:
    print("found")
else:
    print("not found")
'''
'''
s="i am boy"
if 'a' or 'e' or 'i' or 'o' or 'u' in s:
    print("Vowel found")
else:
    print("Vowel not found")
'''
'''
s="In this tutorial, you will learn Spring boot basics and how to build step by step REST APIs using Spring boot. Before understanding what is Spring boot, let's first take a look into what is Spring framework?"
if "you" and "was" in s:
    print("found")
else:
    print("not found")
'''




'''
s="i am boy"
vowels='aeiou'
if any(char in vowels for char in s):
    print("Vowel found")
else:
    print("Vowel not found")
'''
'''
a=[3,6,2,7,9,3,6,9,2]
even=[]
for i in a:
    if i%2==0:
        even.append(i)
print(even)

'''
'''
a=[3,6,2,7,10,3,5,9,2]
a[1],a[2]=a[-2],a[-3]
print(a)
'''

'''
c={}
c[1]="sujith"
c[2]="niranjan"
c[3]="bala"
for i in c.values():
    print(i)
'''

'''
add=0
dict={"A":45,"B":56,"C":67,"Z":43}
for i in dict:
    add=add+dict[i]
print("The addition of values from dict",add)
'''

'''
add=[]
dict={"A":45,"B":56,"C":67,"Z":43}
for i in dict:
    add.append(dict[i])
print(add)
a=sum(add)
print("The addition of values from dict",a)
'''
'''
student_db={}
print("\t\t*** Student Management System ***")
#n=int(input("Total no of student to be add:\t"))
mark=[]
student_db['name']=input("Enter the Student Name:\t")
student_db['age']=int(input("Enter the Student Age:\t"))
for i in range(1,6):
    mark.append(int(input(f"Enter m{i} mark:\t")))
student_db['marks']=mark

print(student_db)

'''

'''
student_db={}
print("\t\t*** Student Management System ***")
n=int(input("Total no of student to be add:\t"))
count=1


while count<=n:
    mark_count=[]
    student_db[f'name_{count}']=input("Enter the Student Name:\t")
    student_db[f'age_{count}']=int(input("Enter the Student Age:\t"))
    for i in range(1,6):        
        mark_count.append(int(input(f"Enter m{i} mark:\t")))
    student_db[f'marks_{count}']=mark_count
    count=count+1

print(student_db)
'''

'''
vowel={"a":"Vowel",
       "e":"Vowel",
       "i":"Vowel",
       "o":"Vowel",
       "u":"Vowel",}
print(vowel.get(input("Enter any character"),"Consonent"))
'''


a={"name":"Arun",
   "age":19,
   "std": 10,
   "marks":[55,66,77,88,44],
   "profile":{"f_name":"raju",
              "f_age":57,
              "f_occu":"driver"} }


print(a["marks"][2])
print("Father age:",a["profile"]["f_age"])












































