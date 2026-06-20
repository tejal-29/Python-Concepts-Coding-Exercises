# write a code that takes a list and a target number, use loop to determine if the target number exists in the list. do not use the in operator.


def target_exists(lst, target):
    for num in lst:
        if num == target:
            return True
    return False
    
nums = [23, 45, 62, -26, -98, 29, 8]

print(target_exists(nums, 92))
print(target_exists(nums, 23))
print(target_exists(nums, 29))
print(target_exists(nums, 0))