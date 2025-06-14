'''
with open('python_class.txt') as file:
   df = file.read()
   print(df)
   '''

'''
#Read file
file = open(r'python_class.txt', 'r')
print(file.read())
file.close()

'''
'''
#create new file
fp = open(r'sales.txt', 'x')
fp.close()
'''
''''
#write text into file
fp = open('sales_2.txt', 'w')
fp.write('Hello')
fp.close()
'''
'''
#write text into file
fp = open('sales_2.txt', 'w')
for i in range(100):
    fp.write("Python class\n")
fp.flush()
fp.close()
'''
'''

#file create 100times
for i in range(100):
    file=open(f"{i}.txt",'x')
'''
'''
for i in range(100):
    try:
        with open(f"{i}.txt", 'x') as file:
            pass  # Do something with the file if needed
    except FileExistsError:
        print(f"File {i}.txt already exists")
'''
    


'''
#delete file
import os
os.remove('1.txt')
print("File deleted sucess fully")

'''

'''
#delete multiple files
import os

for i in range(100):
    file_name = f'{i}.txt'
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"{file_name} deleted successfully")
    else:
        print(f"{file_name} does not exist")

print("Deletion process completed")
'''


'''
# read first line
f = open("sample.txt", "r")
print(f.readline())
print(f.tell())
'''


'''
#Read file name from path

import os
directory = os.path.dirname(__file__)
file_names = os.listdir(directory)

print(file_names)
'''

'''
import os
dir=os.path.dirname(__file__)
for i in os.listdir(dir):
    print(i)
'''

'''
import os

# Get the directory path of the current Python script
directory = os.path.dirname(__file__)
folder_name = "example_folder"
folder_path = os.path.join(directory, folder_name)
os.makedirs(folder_path)

print(f"Folder '{folder_name}' created successfully at '{folder_path}'")

'''
'''
#to create multiple folders
import os
directory = os.path.dirname(__file__)
for i in range(100):
    folder_path = os.path.join(directory, f'{i}')
    os.makedirs(folder_path)
print("Folders are created")
'''
'''
import os
folder_names=['study','entertainmet','music','videos']
directory = os.path.dirname(__file__)
for i in folder_names:
    folder_path = os.path.join(directory, f'{i}')
    os.makedirs(folder_path)
print("Folders are created")
'''

#Delete folders
import os
directory = os.path.dirname(__file__)
for i in range(100):
    folder_path = os.path.join(directory, f'{i}')
    os.rmdir(folder_path)
print("Folders are Deleted")






























