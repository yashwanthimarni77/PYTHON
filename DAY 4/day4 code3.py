# write a python program to print the product of elements in the given matrix
r=int(input("ROWS "))
c=int(input("COLUMNS "))
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
#print(l)
product=1
for r in l:
    print(r)
    for element in r:
        product *= element
print(product)

""" r=int(input("ROWS "))
c=int(input("COLUMNS "))
l=[0]*r
for i in range(r):
    l[i]=list(map(int,input().split()))
#print(l)
product=1
for i in l:
    print(i)
    for j in i:
        product *= j
print(product) """
