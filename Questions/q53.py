# Find the largest element

nums = [9, 14, 5, 34, 41, 56, 69, 73, 88, 90, 109]

maximum = float("-inf")

for num in nums:
    if num > maximum:
        maximum = num

print(f"The maximum number is: {maximum}")