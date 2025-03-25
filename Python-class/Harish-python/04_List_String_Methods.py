#     #1. append():--Add the elemnt to end of list
# Students=['Anbu','Lokesh','swathi','Jana','algets','Rithanya']
# Students.append("Jack")
# print(Students)
# Students.append(100)
# print(Students)


    #2. extend():--merge two list
# marks=[20,45,32,55,67]
# data=[34,56,78]
# marks.extend(data)
# print(marks)



    #3.insert()--insert element using index number
# Students=['Anbu','Lokesh','swathi','Jana','algets','Rithanya']
# Students.insert(3,"Jack")
# print(Students)

    #4.remove()--To remove element from list using value
# Students=['Anbu','Lokesh','swathi','Jana','algets','Rithanya']
# Students.remove("Lokesh")
# print(Students)

    #5. pop()--To Remove elements from the end of list
# Students=['Anbu','Lokesh','swathi','Jana','algets','Rithanya']
# Students.pop()
# print(Students)
# Students.pop(-2)
# print(Students)

    #6. index()--To find index of element in list
# Students=['Anbu','Lokesh','swathi','Jana','algets','Rithanya']
# print(Students.index("swathi"))
 

    #7. count()--To count the number of element in list
# Students=['Anbu','Lokesh','swathi','Jana','algets','Rithanya','swathi']
# print(Students.count("swathi"))

    #8. sort()--To sort the list in ascending order
# numbers=[3,5,6,7,2,3,4,8,9]
# numbers.sort()
# print("Assending Order",numbers)
# numbers.sort(reverse=True)
# print("Dessending Order",numbers)


    #9. split()--split() method using split into a string of list 

# a="Harish is a good boy"
# b=a.split(' ')
# print(b)


# a="Harish is a good boy. He is from kangeyam. Food Donation Management System: A web application which is useful for management of food donation and collection activities."
# sentance=len(a.split('.'))
# print(sentance)

'''
a="Harish is a good boy. He is from kangeyam. Food Donation Management System: A web application which is useful for management of food donation and collection activities."
words=a.split(' ')
words_count=len(a.split(' '))
print(words)
print(words_count)
# for i in words:
#     print(i)

for i in words:
    print(f'{i} = {words.count(i)}')

    
    H/W==count of each charactor
'''

# Problem: Game === geuss no(1 to 10)

# import random

# while True:
#     user_input=int(input("Guess any number between 1 to 10\t"))
#     gen_no=random.randint(1,10)
#     if user_input==gen_no:
#         print("Congratulations! You guessed the correct number.")
#     else:
#         print("You guessed is wrong number.")
#         print(f"Number is {gen_no}")
    

# import random
# for i in range(10):
#     a=random.randint(1,10)
#     print(a)


# Problem: 4digit otp

import random

for i in range(20):
    otp=random.randint(1000,9999)
    print(otp)