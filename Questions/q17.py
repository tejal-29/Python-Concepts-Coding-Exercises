#SUm of all the numbers from 1 to 100 divisible by 2 and 7

start = int(input("enter a start: "))
end = int(input("enter a end: "))

i = start
total = 0
while i <= end:
    if i % 2 == 0 and i % 7 == 0:
        print(i, end=" ")
        total = total + i
    i += 1

print(f"\nTotal = {total}")
