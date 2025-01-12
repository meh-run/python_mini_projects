n=int(input("enter an integer number"))
for i in range (2,n):
    if(n%i==0) :
     print("not prime")
else:
     print("is prime")