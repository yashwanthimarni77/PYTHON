#check if the number is strong number or not using functions
def strong_number(n):
    x,sum=n,0
    while n>0:
        digit=n%10
        fact = 1
        for i in range (1,digit+1):
            fact*=i
        sum+=fact
        n//=10
    if sum == x:
        return "Strong Nunmber"
    else:
        return "Not a Strong number"
n=int(input())
print(strong_number(n))
