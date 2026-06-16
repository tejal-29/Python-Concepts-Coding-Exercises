age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible for vote")
else: 
    print("You are not eligible")



physics = int(input("enter physics marks: "))
bio = int(input("enter bio marks: "))

if physics >= 35 and bio >= 35:
    print("You are pass")
else:
    print("You failed")


marks = int(input("Enter your total marks: "))

if marks >= 90 and marks <= 100:
    print("grade A")
elif marks >= 75:
    print("grade B")
elif marks >= 60:
    print("grade C")
elif marks >= 45:
    print("grade D")
else:
    print("you are failed")