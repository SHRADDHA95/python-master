import sys

print(sys.setrecursionlimit(10))

print(sys.getrecursionlimit())


def decrement(n):

    print("Hello", n)
    if n == 0:
        return

    decrement(n-1)

decrement(50)