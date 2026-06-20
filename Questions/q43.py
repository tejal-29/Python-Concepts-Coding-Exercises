'''
write a function called absolute_value that takes a number and returns 
its absolute value without using the built-in abs() function
'''
#if number is negative or positive is always ives positive number is called absolute number
# abs() it is a buil i function in python for absolute 

def absolute_value(num):
    if num >=0:
        return num
    return num * -1

n = int(input("Enter the value: "))
print(f"The abs is : ", absolute_value(n))