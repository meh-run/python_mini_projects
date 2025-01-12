i=int(input("enter a number  "))
def fibonacci (i):
    m=0
    t=1
    if i<=2 :
        return 1
    else:
        for c in range(i):
            n=m+t
            m=t
            t=n
        return t

print(fibonacci(i))
