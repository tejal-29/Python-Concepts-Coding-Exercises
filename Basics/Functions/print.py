#take input name , gender and age and print

def people(name, gender, age):
    print(f"Hello {name}!! you are a {gender}, and your age is {age}")


n = input("Enter your name: ")
g = input("enter your gender: ")
a = int(input("enter your age: "))
people(n, g, a)