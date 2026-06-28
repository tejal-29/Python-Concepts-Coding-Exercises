'''
write a program that takes a list of numbers and using a loop 
determines whether it is sorted in ascendind order. print True if it is sorted and false otherwise
'''

def is_sorted(lst):
    n = len(lst)
    for i in range(0, n-1):
        if lst[i] > lst[i + 1]:
            return False
    return True

num = [29, 9 , 3, 30, 12, 95, 1, 97, 21, 81, 86, 75, 6, 4]
ans = is_sorted(num)
print(f"List sorted -> {ans}")
