#print average without using direct function

def calculate_average(lst):
    n = len(lst)
    total = 0
    for num in lst:
        total += num
    return total / n

nums = [23, 45, 62, -26, -98, 29, 8]
ans = calculate_average(nums)
print(f"The Average is: {ans:.2f}")