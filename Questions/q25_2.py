n = int(input("enter a num: "))

for i in range(1, n+1):
    for j in range(n, i-1, -1):   #if i = 0 so : 5, 1-1 , -1 :.  
        print(j, end=" ")
    print()