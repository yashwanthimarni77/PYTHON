#write a python program to print sum of the given matrix.
"""r=int(input("ROWS "))
c=int(input("COLUMNS "))
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
print(l)"""

"""r=int(input("ROWS "))
c=int(input("COLUMNS "))
l=[]
total_sum=0
for i in range(r):
    l.append(list(map(int,input().split())))
    total_sum=sum(sum(r)for r in l)
print(total_sum) """  

r=int(input("ROWS "))
c=int(input("COLUMNS "))
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))    
#print(l)
total_sum=0
for i in l:
    print(i)
    total_sum+=sum(i)
print(total_sum)
