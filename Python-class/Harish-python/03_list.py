# a=[] #empty list

#Slicing Method
# Students=['Anbu','Lokesh',100,'swathi','Jana',False,'algets','Rithanya',True]
# print(Students[5:7])
# print(Students[:4])
# print(Students[3:5])



# Students=['Anbu',[1,3,5,7],'Lokesh',100,'swathi',[1,3,5,7],'Jana',False,'algets','Rithanya',True]
# print(Students[1])
# # #Read data from nested list
# print(Students[1][2])
# print(Students[5][3])

#List Methods:
    #1. append():--Add the elemnt to end of list
Students=['Anbu','Lokesh','swathi','Jana','algets','Rithanya']
Students.append("Jack")
print(Students)
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

    #5. pop()--To Remove elements from end of list
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

#9. clear()

# numbers=[3,5,6,7,2,3,4,8,9]
# numbers.clear()
# print(numbers)

# del numbers
# print(numbers)

#List Functions:
        #1. max()
# numbers=[3,5,6,7,2,9,3,4,8]
# print("Max Value:",max(numbers))

        #2. min()
# numbers=[3,5,6,7,2,9,3,4,8]
# print("Min Value:",min(numbers))

        #3. sum()
# numbers=[3,5,6,7,2,9,3,4,8,5,34,56]
# print("Sum of the numbers:",sum(numbers))
# print("Avg of the numbers:",sum(numbers)/len(numbers))





