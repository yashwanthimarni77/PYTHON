#write a python program to print amstrong number in a range using functions.
'''def is_armstrong(num):
    order = len(str(num))
    sum=0
    temp=num
    while temp > 0:
        digit = temp%10
        sum += digit**order
        temp //= 10
    return num== sum
def armstrong_in_range(start,end):
    for num in range(start,end+1):
        if is_armstrong(num):
            print(num)

armstrong_in_range(100,10000)'''

def armstrong(n,m):
    for i in range(n,m+1):
        sum=0
        x=i
        while i>0:
            temp=i%10
            sum+=temp**3
            i//=10
        if sum==x:
            print(x)

n=int(input())
m=int(input())
armstrong(n,m)
