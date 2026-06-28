'''
given two lists of the same length, write python code using a loop to create a new lists where each elements is the sum of the correspoding
elements from the both original lists.
'''
def sum_of_two_list(lst1, lst2):
    new_list = []
    n = len(lst1)
    for i in range(0, n):
        total = lst1[i] + lst2[i]
        new_list.append(total)
    return new_list    

num1 = [4, 7, 3, -9, 6, 12, 16]
num2 = [7, 13, 6, 8, 5, 10, 1]
ans = sum_of_two_list(num1, num2)
print(f"The new list {ans}")

