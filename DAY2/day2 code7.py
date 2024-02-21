#wrute a program to check the given number is amstrong number
'''a = int(input()) #168
rev= 0
while a > 0:
    digit=a%10 #8=6=1
    rev=rev*10+digit #86
    a//=10 #16=1=0
print(rev)'''

a = int(input())
temp=a
rev= 0
while a > 0:
    digit=a%10
    rev=rev+digit**3
    a//=10
if rev == temp:
    print("Amstrong")
else:
    print("Not an Amstrong")
