num = int(input("Enter the Number: "))

# if num >= 18 :
#     print(f"eligible to vote")
# else :
#     print(f"not eligible to vote")

eligible = num >= 18
senior_citizen = num >= 60

print(f"User is eligible for vote: {eligible}")
print(f"User is senior citizen: {senior_citizen}")