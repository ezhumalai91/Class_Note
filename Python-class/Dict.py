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
#print(b.values())
b.update(name4="mani")
print(b)

b.clear()
print(b)
'''

'''
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict['class']['student']['marks']['history'])

'''
employees = ['Kelly', 'Emma',"Mani"]
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)












