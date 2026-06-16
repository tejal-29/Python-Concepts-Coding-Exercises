#Take two numbers as input. Without using *, calculate and print their product using += in a way that adds the first number to itself the second number of times.

num1 = int(input())
num2 = int(input())

product = 0

for i in range(num2):
    product += num1
print(product)