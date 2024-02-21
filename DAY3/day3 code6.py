#write a python program to print armstrong number in a range using strings and functions
"""def is_armstrong(num):
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

armstrong_in_range(100,10000)"""

def armstrong(n,m):
    for i in range(n,m+1):
        s=str(i)
        sum=0
        for j in s:
            sum+=int(j)**len(s)
        if str(sum)==s:
            print(i)
n=int(input())
m=int(input())
armstrong(n,m)
