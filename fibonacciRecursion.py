
def fibonacci_recursion(num, fib_series):
    if num < 2:
        return fib_series

    length = len(fib_series)
    num_new = fib_series[length-1]+fib_series[length-2]
    fib_series.append(num_new)
    return fibonacci_recursion(num-1, fib_series)



result = fibonacci_recursion(10, [0,1])
print(result)