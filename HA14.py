#1
def f1(n, a=0):
    return int(n % 10) + f1(int(n / 10))

import sys
sys.setrecursionlimit(10000)

f1(12)

#2
def f2(n):
    return n + f2(n - 1)

f2(12)

#3
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
fibonacci(6)