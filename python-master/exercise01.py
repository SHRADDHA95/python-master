#1
num_input = range(1,70)
for num in num_input:
    if (num==63):
        break
    if(num%7==0):
        continue    
    #print("num is ", num)

#2 
num_orginal = range(10)
num_cubes = [x ** 3 for x in num_orginal if x%3==0]
print("OUTPUT :" , num_cubes)