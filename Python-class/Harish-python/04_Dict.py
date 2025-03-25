#empty Dict
# library={}
# a=dict()


# library={'book_name':"Harry Patter",'book_sub':"History",'book_count':50,'fifth_std':['Hari','Arun','Harini']}
# print(library)
# print(library['book_sub'])
# print(library['book_name'])
# library['marks']=[467,387,499]
# print(library)
# print(library['fifth_std'][1])

sampleDict = {
    "class":{"student":
             {"name":"Mike","marks": {"physics": 70,"history": 80},'name1':"Anbu","marks1": {"physics": 90,"history": 70}}
              }
              }
# print(sampleDict['class']['student']['marks']['history'])
print(sampleDict['class']['student']['marks1']['physics'])