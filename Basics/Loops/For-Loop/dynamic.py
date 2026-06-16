start = int(input("enter a start: "))
end = int(input("enter a end: "))

total = 0
for i in range(start, end + 1):
    if i % 2 == 0:
        print(i, end=" ")
    total += i

print(f"\nTotal: {total}")    
