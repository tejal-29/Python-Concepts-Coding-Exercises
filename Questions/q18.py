'''
ask a number from user, print the multiplication table upto 10.


enter a num = 2
 2 x 1 = 2
 2 x 2 = 4
 2 x 3 = 6
 ....
 2 x 10 = 20

 '''
num = int(input("enter a num = "))

i = 1
while i <= 10:
    print(f" {num} x {i} = {num*i}")
    i += 1