# li=[2, 5, 7, 8, 10]
# even=[]
# for i in li:
#     if i%2==0:
#         even.append(i)
# #print(even)
# count=len(even)
# print(f"Count of even number from list {count}")


# a=[1, 2, 3]
# sq=[]
# for i in a:
#     sq.append(i*i)
# print(sq)

# a=[2, 3, 4]
# product=1
# for i in a:
#     product=product*i


# a=[2, 3, 4,56,34,2,6,7,8,89]
# summ=0
# for i in a:
#     summ=summ+i
# print(summ)


# a=[5, 10, 15]
# for i in a:
#     print(f"Index {a.index(i)}: {i}")


# a=[10, 20, 30]
# print(a[::-1])

# #to find doublicate no
a=[1, 2, 3, 2, 4, 3]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            print(f"Doublicate no is {a[i]}")