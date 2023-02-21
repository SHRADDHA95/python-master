# exhange the value of 2 numbers without using third variable
first_number = int(input("input first number : "))
second_number = int(input("input second number : "))
first_number = first_number + second_number
second_number = first_number - second_number
first_number = first_number - second_number
print("\nafter swapping first_number is :", first_number, "\n second_number is :", second_number)
