start = int(input("enter start num: "))
end = int(input("enter end num: "))

i = start
while i <= end:
    if i %2 ==0:
        print(i, end=" ")
    i +=1

