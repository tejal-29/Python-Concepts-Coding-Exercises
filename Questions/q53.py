# Find the largest element without using max()

nums = [9, 14, 5, 34, 41, 56, 69, 73, 88, 90, 109]

maximum = float("-inf") #it is a smallest value to compare any value in number data types i.e float of (-infinity)

for num in nums:
    if num > maximum:  #check number is greater than max
        maximum = num  #it will update maximum value

print(f"The maximum number is: {maximum}")