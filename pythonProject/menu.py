def fact(f):
    flag = 1
    for i in range(f):
        flag *= i + 1
    return flag


def fib(fn):
    n1 =0
    n2 = 1
    for i in range(fn):
        nth = n1 + n2
        n1 = n2
        n2 = nth
        print(n1)


def gcd(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if (x % i == 0) and (y % i == 0):
            gcd = i
    return gcd


def cal_age(n):
    m=2023-n
    return m


print(''' python project 1 
    1. factorial
    2. fibonacci
    3. gcd
    4. cal_age
    5. exit
''')
num = int(input())
while num != 5:
    if num>5 :
        print("please enter a number only between 1 and 5")
    if num == 1:
        print('write a number')
        f = int(input())
        print(fact(f))
        print('''python project 1
            1. factorial
            2. fibonacci
            3. gcd
            4. cal_age
            5. exit
        ''')
        num = int(input())
        if num > 5:
            print("please enter a number only between 1 and 5")
    elif num == 2:
        print('write a number')
        fn = int(input())
        fib(fn)
        print('''python project 1
            1. factorial
            2. fibonacci
            3. gcd
            4. cal_age
            5. exit
        ''')
        num = int(input())
        if num > 5:
            print("please enter a number only between 1 and 5")
    elif num == 3:
        print('write two number')
        n1 = int(input())
        n2 = int(input())
        print(gcd(n1, n2))
        print('''python project 1
            1. factorial
            2. fibonacci
            3. gcd
            4. cal_age
            5. exit
        ''')
        num = int(input())
        if num > 5:
            print("please enter a number only between 1 and 5")
    elif num == 4:
        print("enter age in Gregorian years")
        n = int(input())
        print(cal_age(n))
        print('''python project 1
            1. factorial
            2. fibonacci
            3. gcd
            4. odd or even
            5. exit
        ''')
        num = int(input())
        if num > 5:
            print("please enter a number only between 1 and 5")
    elif num > 5:
        print('''python project 1
            1. factorial
            2. fibonacci
            3. gcd
            4. odd or even
            5. exit
        ''')
        num = int(input())
