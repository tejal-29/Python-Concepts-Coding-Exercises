# Write a function called find_max that takes three numbers as parameters and print the largest one.

def find_max(n1, n2, n3):
    if n1 > n2 and n1> n2:
        print(n1)
    elif n2 > n1 and n2 > n3:
        print(n2)
    elif n3 > n1 and n3 > n2:
        print(n3)
    else:
        print("Invalid numbers")    

num1 = int(input("enter 1: "))
num2 = int(input("enter 2: "))
num3 = int(input("enter 3: "))

find_max(num1, num2, num3)