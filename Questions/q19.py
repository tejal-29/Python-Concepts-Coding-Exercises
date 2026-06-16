'''
ask a number from user, and print all the factors

enter a number = 10
1 2 5 10

enter a number = 100
1 2 4 5 10 20 25 50 100
'''

num = int(input("Enter a number: "))

i = 1
while i <= num:
    if num % i == 0:
        print(i, end=" ")
    i += 1