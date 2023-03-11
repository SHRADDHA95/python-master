
def square_generator(limit):
    for i in range(2, limit):
        yield i**2


itr_square = square_generator(10)
print("from single iterator :" , next(itr_square))

print("from list :" , list(itr_square))

for country in "Germany","India","Israel":
    print(country)


cars_list = ['Toyota Camry',  'Honda Accord', 'Honda Civic', 'Toyota Corolla']
cars_list[4] = 'Hyundai Elantra'

def subtract(x,y):
    print("new")


r = subtract(100, 50)
print(r)


tup= (2, 4.6789 , 'ne',True)
print("%d %0.2f %s %s" %tup)

name ="shraddha"
print(f'my name is {name} ')



