### while loop in python ####


while True:
    egypt_capital = str(input("Enter the capital of Egypt :"))
    if (egypt_capital == "quit"):
        print("\n The correct answer is Cairo , better luck next time!")
        break
    if (egypt_capital.upper() == 'Cairo'.upper()):
        print("\n That is the correct answer.")
        break
    else:
        print("\nPlease enter the correct answer , Try again....")

else:
    x =2
    print("done")