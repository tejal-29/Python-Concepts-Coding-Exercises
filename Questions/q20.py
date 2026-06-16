'''
Take numbers as input from the user one by one. Skip negative numbers
and keep adding the positive ones. stop when the user enters 0 and  
print the total. (Uses both contiue and break)
'''

total = 0
while True:
    num = int(input("enter a num: "))
    if num == 0:
        break
    if num < 0:
        continue
    total += num

print(total)