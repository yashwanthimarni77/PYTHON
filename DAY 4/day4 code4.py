#write a python program to print sum of max and min elements in a matrix using tuple.
''' r=int(input("ROWS "))
c=int(input("COLUMNS "))
t=[]
for i in range(r):
    t.append(tuple(map(int,input().split())))
#print(t)
t=[element for r in t for element in r]
result_tuple=(max(t),min(t))
sum=sum(result_tuple)
print(sum) '''

r=int(input("ROWS "))
c=int(input("COLUMNS "))
l=[]
for i in range(r):
    l.append(tuple(map(int,input().split())))
#print(l)
min,max=1000,0
for i in l:
    print(i)
    for j in i:
        if j>max:
            max=j
        if j<min:
            min=j
print(max+min)
