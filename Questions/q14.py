amount = int(input("Enter your total purchase amount: "))

# if amount > 5000:
#     print("you will get 20% discount ")
# elif amount > 2000:
#     print("you will get 10% discount")
# elif amount > 1000:
#     print("you will get 5% discount")
# else:
#     print("no discount")

if amount > 5000:
    discount = amount * 20 / 100
    print("You will get 20% discount")
elif amount > 2000:
    discount = amount * 10 / 100
    print("You will get 10% discount")
elif amount > 1000:
    discount = amount * 5 / 100
    print("You will get 5% discount")
else:
    discount = 0
    print("No discount")

final_amount = amount - discount

print("Discount Amount:", discount)
print("Final Amount to Pay:", final_amount)