'''
#To Merge to sets
x1 = {'foo', 'bar', 'baz','qux'}
x2 = {'baz', 'qux', 'quux'}
x3=x1|x2
print(x3)

#other method

x4=x2.union(x1)
print(x4)

#To find common
x=x1 & x2
print(x)

x5=x1.intersection(x2)
print(x5)
'''
'''
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}
res=a.intersection(b, c, d)
print(res)
'''
'''
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
res=x1.difference(x2)   #x1-x2
print(res)
'''

x1 = {'foo', 'bar', 'baz'}
x2={'foo', 'bar', 'baz', 'qux', 'quux'}
res=x1.issubset(x2)
print(res)




























