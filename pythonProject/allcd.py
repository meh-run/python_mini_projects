n =5
def fibonacci(n):
    if n<= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
x=0
for i in range(1,n+1):
    x = x + (i-1)*(i-2)/2
print(fibonacci(n))
print(x)
