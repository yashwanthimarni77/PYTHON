#Write a python to print the reverse of the number using while loop
a = int(input())
rev= 0
while a > 0:
    digit=a%10
    rev=rev*10+digit
    a//=10
print(rev)
