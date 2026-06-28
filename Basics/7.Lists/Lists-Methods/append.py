# Add a element to the end of List

nums = [9, 30, 29, 3, 78]
nums.append(100)
nums.append("OKoee")
print(nums)

# insert the element
nums.insert(0, "tejal")
print(nums)

# Pop the element
nums.pop()
print(nums)

# Pop the element using index
nums.pop(4)
print(nums)

# remove the element from list
nums.remove(78)
print(nums)

nums.remove(21)
print(nums)      #ValueError: list.remove(x): x not in list