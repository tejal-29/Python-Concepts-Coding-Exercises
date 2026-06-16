age = int(input("Enter your age: "))
photo_ID = input("You have a valid ID (True/False): ").lower() == "true"


if age >= 18 and photo_ID == True:
    print("You can enter a venue")
else:
    print("You cannot enter a venue")