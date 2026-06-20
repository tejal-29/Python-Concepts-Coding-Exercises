marks = [29, 40, 59, 24, 36]

#to get length
n = len(marks)
print(f"Length of list is: {n}")

#Max 
maximum = max(marks)
print(f"The max num is: {maximum}")

#Min
minimum = min(marks)
print(f"the min num is: {minimum}")

#sum 
total = sum(marks)
print(f"the sum of all num are: {total}")

#ascending 
ascending = sorted(marks)
print(f"the ascending order is: {ascending}")

#descending 
descending = sorted(marks, reverse=True)
print(f"List in descending order: {descending}")

average = sum(marks) / len(marks)
print(f"the average of list is: {average}")