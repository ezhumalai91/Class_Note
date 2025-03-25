#Dict

#a={}  #Empty dic

'''
b={'1': 'Geeks', '2': 'For', '3': 'Geeks'}
print(b)
print(b['3'])
'''
'''
b={'name1': 'priya', 'name2': 'Dhivya', 'name3': 'Mahi'}
print(b)
print(b['name3'])
'''
#Python Dictionary Methods

'''
b={'name1': 'priya', 'name2': 'Dhivya', 'name3': 'Mahi'}

for i in b:
    print(i)

for i in b.values():
    print(i)

for i in b.keys():
    print(i)

for key,value in b.items():
    print(key, "=", value)
'''

'''
b={'name1': 'priya', 'name2': 'Dhivya', 'name3': 'Mahi'}
#b.pop("name3")
print(b)
b.popitem()
print(b)
'''

'''
b={'name1': 'priya', 'name2': 'Dhivya', 'name3': 'Mahi'}
print(b.values())
b.update(name4="mani")
print(b)

b.clear()
print(b)
'''




sampleDict = {
    "class": {
        "student": {
                            "name": "Mike",
                            "marks": {
                                    "physics": 70,
                                    "history": 80,
                                    "tamil":100
                                            },
                            "dress_code":[4,5,6,7,8]
                            }
                }
}
print(sampleDict['class']['student']['marks'])
print(sampleDict['class']['student']['marks']['history'])
print(sampleDict['class']['student']['dress_code'][2])



'''
employees = ['Kelly', 'Sheela',"Mani"]
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)

'''

'''
j,s,e=["anbu","mani","nirmal","jack"],["a","b","c","d"],["q","w","r"]
j_sal,s_sal,e_sal={"designation": 'junior Developer', "salary": 8000},{"designation": 'senior Developer', "salary": 15000},{"designation": 'expert Developer', "salary": 20000}
j_res = dict.fromkeys(j, j_sal)
s_res=dict.fromkeys(s,s_sal)
e_res=dict.fromkeys(e,e_sal)
print(j_res)
print(s_res)
print(e_res)

'''









