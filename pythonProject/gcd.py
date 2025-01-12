n = int(input())
m = int(input())
def GCD (n ,m):
    if m==0 :
        return n
    if n==0 :
        return m
    if m==n :
        return m
    if m>n :
        return GCD(n-1 ,m)
    return GCD(n ,m-1)

if GCD(n,m) :
    print(f"GCD of {n} and{m} is{GCD(n,m)}")
else:
    print("dont have gcd")