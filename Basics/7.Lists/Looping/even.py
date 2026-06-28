num = [1, 2, 4, 23, 29, 34, 48, 51, 67, 7, 85, 98, 100]

n = len(num)
i = 0
count = 0

while i <= n - 1:
    if num[i] % 2 == 0:
        count += 1
    
    i += 1
    

print(count)