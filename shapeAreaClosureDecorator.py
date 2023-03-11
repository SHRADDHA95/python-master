def shapeArea_calculator(func):
    def calculate(*dimensions):
        for dimension in dimensions:
            if dimension <= 0:
                return "dimension of a shape should be positive integer."
        return func(*dimensions)
    return calculate

@shapeArea_calculator
def area_of_rectangle(length , height):
    return length * height

@shapeArea_calculator
def area_circle(radius):
    return 3.14 * radius ** 2

print(area_of_rectangle(10,20))
print(area_circle(7))
