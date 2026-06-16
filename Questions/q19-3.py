'''
ask a number from user, and count all the factors divisible by 5

enter a number = 10
1 2 5 10
count = 4

enter a number = 100
1 2 4 5 10 20 25 50 100
count = 9
'''
num = int(input("enter a num: "))

i = 1
count = 0
while i <= num:
    if num % i == 0 and i % 5 == 0:
        print(i, end=" ")
        count = count + 1
    i += 1

print(f"\nTotal factors of {num} are: {count}")