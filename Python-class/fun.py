

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
'''
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

print("The addition is",add(5,6))

'''

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
'''

H/W:

display(ramya,21,45.6)
display(raja)

    















































    




















