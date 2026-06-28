# clear the elements from the list

fruits = ["Mango", "banana", "Cherry", "apple"]
fruits.clear()
print("After the clearing the elements from the list: ",fruits)


# create a shallow copy of the list
og_list = [10, 30, 60]
new_list = og_list.copy()

new_list.append(100)
print("Original list: ",og_list)
print("New List: ",new_list)