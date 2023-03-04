# pattern 10 +1010+101010
in_number = int(input("input number : "))
temp1 = str(in_number)
temp2 = temp1 + temp1
temp3 = temp1 + temp1 + temp1
total = in_number + int(temp2) + int(temp3)
print("total sum is : ", total)
