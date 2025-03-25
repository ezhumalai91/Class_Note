'''
# Multiplication table
for row in range(10):
    for col in range(10):
        num = row * col #
        if col == 0:
            if row == 0:
                print("    ", end='')
            else:
                print("  ", row, end='')
        elif row == 0:
           print("  ", col, end='')
        else:
            print(" ", num, end='')
    print()
'''

'''
mult_table = [
    [1, 2, 3,4],
    [2, 4, 6,8],
    [3, 6, 9,12],
    [4,8,12,16]
]

for row in mult_table:
    #print(row)
    print("\t" .join(map(str, row)))
'''

'''
rows = 6
for i in range(rows):
    for j in range(i):
        print(i, end=' ')
    print('')
'''

'''
rows=5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')
'''

'''
for i in range(5):
    for j in range(5):
        print("*",end='  ')
    print()
'''

'''
for i in range(5):
    for j in range(5):
        if i==j:
            print("*",end='  ')
        else:
            print(" ",end='  ')
    print()
 '''  
for i in range(5):
    for j in range(5):
        if i==0 or j==0:
            print("*",end='  ')
        else:
            print(" ",end='  ')
    print()
























    









    
