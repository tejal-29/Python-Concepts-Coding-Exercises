'''
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
'''

for i in range(1, 6):          
    for k in range(1, 6-i):
        print(" ", end=" ")
    for j in range(1, i+1):
        print(j, end=" ")
    print()


'''
i = rows  j = column(1, i+1) space  (5-1)      
i = 1        1 to 1            4
i = 2        1 to 2            3
i = 3        1 to 3            2
i = 4        1 to 4            1
i = 5        1 to 5            0
'''    