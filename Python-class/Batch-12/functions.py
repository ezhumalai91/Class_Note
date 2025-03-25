#Function
# Defenition
# It is a set of statements that when called perform a specific task

'''
#Syntax

def fun_name():
    body of the statements
'''

#Without arg and without return value
'''
def hi():
    print("How are you")

n=input("Type any thing to chat\t")
if n.lower()=="hi":
    hi()
'''

#With arg and without return value
'''
def add(a,b):
    c=a+b
    print("The Addion is ",c)

a=int(input("Enter A value"))
b=int(input("Enter B value"))
add(a,b)
add(6,8)
add(56,67)
'''


#Without arg and with return value
'''
def add():
    a=int(input("Enter A value"))
    b=int(input("Enter B value"))
    return a+b
    
print("The Addion is ",add())
'''

#With arg and with return value

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b

# print("The addition is",add(5,6))
# print("The sub is",sub(10,20))


'''
def withdraw(avl_bal):
    amt=int(input("Please enter the withdraw amount"))
    if  amt<=avl_bal:
        avl_bal -= amt
        print(f"{amt} is withdraw successful")
        print(f"Your available balance is ",avl_bal)
        option(avl_bal)
    else:
        print("Insufficiant balance")
        print("Please enter valiable amt")
        withdraw(avl_bal)

def option(avl_bal):
    ch=int(input("1. Withdraw amt\n2.deposite\n3.check balance\n4.Exit\n"))
    if ch==1:
        withdraw(avl_bal)
    elif ch==4:
        exit()
    
def login(avl_bal,password):
    pin=int(input("Enter your pin"))
    if pin==password:
        option(avl_bal)
    else:
        print("Invalid PIN!! Please try again!!")
        login(avl_bal,password)
        
if __name__ == "__main__":
    print("\t\t***ATM Program***")
    avl_bal=10000
    password=1234
    login(avl_bal,password)
'''


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
#Over loading
'''
def add(x,y):
    return x+y
def add(x,y,z):
    return x+y+z
def add(x,y,z,w):
    return x+y+z+w

print("The addition is ",add(2,5))
print("The addition is ",add(2,5,5))
print("The addition is ",add(2,5,3,4))
'''

'''
# function with default argument
def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)

show_employee("Ben", 12000)
show_employee("Jessa")
'''


'''
def add(x=2,y=5,z=10):
    return x+y+z
print(add(3,4,5))
print(add(5))
print(add())
print(add(z=17))
'''

'''
H/W:

display(ramya,21,45.6)
display(raja)
'''
    
'''
def large_finder(n):
    large=n[0]
    for i in  n:
        if large<i:
            large=i
    return large


l=[1,2,3,4,5,55,33,99,5]

print(f"largest no is {large_finder(l)}")
'''




def high_Mark(a):
    t_mark={}
    for name,marks in a.items():
        #print(name,marks)
        t_mark[name]=sum(marks)
    #print(t_mark)
    # find_high_Mark(t_mark)
    #to find max mark from t_mark
    max_mark=max(t_mark.values())
    for i in t_mark:
        if t_mark[i]==max_mark:
            print(f"highest mark is {max_mark} from {i}")

  
        
a={"Niranjan":[78,45,67,87,67],"Sujith":[67,45,39,56,78],"Joe":[67,45,39,56,79],"Nitish":[78,66,35,99,67]}
high_Mark(a)


'''
def count_sent(n):
    count=0
    for i in n:
        if i.endswith('.'):
            count+=1
    return count

def count_word(n):
    count=0
    for i in n:
         if i.endswith(' '):
            count+=1
    return count

def count_char(n):
    count=0
    for i in n:
        count+=1
    return count

n=input("Enter any string")
while True:
    ch=int(input("1. Count of the sentance\n 2. Count of the Word\n 3. Count of the Char"))
    if ch==1:
        print(f"Count of sentance is {count_sent(n)}")
    elif ch==2:
        print(f"Count of Words is {count_word(n)}")
    elif ch==3:
        print(f"Count of char is {count_char(n)}")


'''
