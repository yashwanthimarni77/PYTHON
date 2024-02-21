#write a python program to print the numbers which are not divisible by 6,7,8 in a gven range
n,m=int(input()),int(input())
i=n
while i <= m:
    if i%6!=0 and i%7!=0 and i%8!=0:
        print(i)
    i+=1

        
        
    
    
    
    
