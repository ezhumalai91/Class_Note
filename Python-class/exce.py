#Merge two Python dictionaries into one
'''
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50,'Ten': 1000}

new_dic = {**dict1, **dict2}
new_withdoublicate={**dict1, **dict3}
print("New_dic",new_dic)
print("New_withdoublicate",new_withdoublicate)

'''
'''
db1={"s_name":"Bala",
     "s_dob":"11-11-1999",
     "s_cgpa":7.8,
     "s_class":"First class"}
teacher1={"t_name":"Hari",
     "t_dob":"11-11-1999",
     "t_desg":"HOD",
     "t_salary":30000}

for (key,value) in {**db1,**teacher1}.items():
    print(key,"\t:\t",value)
    
'''

'''
#other method
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)
'''

'''
#Print the value of key ‘history’ from the below

dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            },
            "avg":[23.5,56.3,78.4]
        }
    }
}

print(dict["class"]["student"]["marks"]["history"])
print(dict["class"]["student"]["avg"][1])

'''

'''
jr_employees=["prashant","raju"]
sr_employees = ['Kelly', 'Emma']
sr_emp_salary = {"designation": 'Sr_Developer', "salary": 8000}
jr_emp_salary = {"designation": 'Jr_Developer', "salary": 15000}

result = dict.fromkeys(jr_employees, jr_emp_salary)
sr_result = dict.fromkeys(sr_employees, sr_emp_salary)
print(result)
print(sr_result)
'''

#Create a dictionary by extracting the keys from a given dictionary

sampleDict = { 
  "name": "Kelly",
  "age":25, 
  "salary": 8000, 
  "city": "New york" }

keys = ["name", "salary"]

newDict = {k: sampleDict[k] for k in keys}
print(newDict)






















