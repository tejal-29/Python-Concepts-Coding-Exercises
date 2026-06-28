#       0   1   2   3   4  5  6   7   8   9   10  11  12  13
#   -14  -13  -12 -11 -10 -9 -8  -7 -6  -5  -4  -3   -2   -1 
lst = [29, 30, 45, 82, 49, 9, 1, 90, 78, 92, 49, 120, 49, 21]

lst1 = lst[0:6]
lst2 = lst[5:8]
lst3 = lst[0:14]
lst4 = lst[1:99]         #if the the excluxive doesn't exit then it will print all element till the end 
lst5 = lst[0:1]
lst6 = lst[1:1]          # it will print empty list if both inde are same
lst7 = lst[3:]           # it print all index after the include
lst8 = lst[:13]          # if print all index before the exclude

print(lst1)
print(lst2)
print(lst3)
print(lst4)
print(lst5)
print(lst6)
print(lst7)
print(lst8)

lst9 = lst[0:14:2]
lst10 = lst[4:12:3]
print(lst9)
print(lst10)

lst11 = lst[8:2:-1]
lst12 = lst[9:1:-2]
lst13 = lst[ : :-3] 
print(lst11)
print(lst12)
print(lst13)