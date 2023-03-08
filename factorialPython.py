
def recursive_factorial(num):
    if num < 0:
        return "factorial cannot be calculated for negative numbers!"

    if num == 1:
        return 1

    return num * recursive_factorial(num-1)

n = int(input("enter the number for which you want to calculate factorial! \n"))
print(recursive_factorial(n))