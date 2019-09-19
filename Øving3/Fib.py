def fib(itr):
    a=0
    b=1
    fib = 0
    for i in range(itr + 1):
        fib = a
        a = b
        b += fib
    return fib


def fib_sum(itr):
    a=0
    b=1
    fib = 0
    ans = 0
    for i in range(itr + 1):
        fib = a
        ans += fib
        a = b
        b += fib
    return ans


def fib_list(itr):
    a=0
    b=1
    fib = 0
    ans = []
    for i in range(itr + 1):
        fib = a
        ans.append( fib )
        a = b
        b += fib
    return ans


print(fib_list(10))
