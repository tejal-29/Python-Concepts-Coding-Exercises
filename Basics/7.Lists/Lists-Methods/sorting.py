# Sorting elements

lst = [23, 16, 32, 29, 47, 58, 63, 72, 79, 25, 12]
lst.sort()
print(lst)

# Sorting in descending order
lst.sort(reverse=True)
print(lst)

# reverse the elements
lst2 = [10, 30, 40, 20 , 80, 50, 100]
lst2.reverse()
print(lst2)



# sort vs sorted
# sorted is built in function     (id will change)
# sort is method, it is a in-place sorting  (id will remain same)

print(f"nums = {lst}", id(lst))
lst.sort()
print(f"nums = {lst}", id(lst))


new_list = sorted(lst)
print(f"new nums = {new_list}", id(new_list))
