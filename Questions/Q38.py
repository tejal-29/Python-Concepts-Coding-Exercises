# Write a function called reactangle_area that takes length and breadth

def reactangle_area(length, breadth):
    area = length*breadth
    print(f"The are of {length} and {breadth} is {area}")

l = int(input("enter length: "))
b = int(input("enter breadth: "))

reactangle_area(l, b)