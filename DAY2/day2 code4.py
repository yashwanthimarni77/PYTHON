#check the number is prime or not
n=int(input("Enter a number "))
counter=0
for i in range(1,n):
    if n%i==0:
        counter=counter+1
if counter==1:
    print("Prime")
else:
    print("Not a Prime number")
        
    
