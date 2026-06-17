#Write a function that ask a number from user and prints it that number is odd or even

def odd_even():
    num = int(input("enter a num: "))
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

odd_even()