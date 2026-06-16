marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("grade A")
elif marks >= 75 and marks <= 89:
    print("grade B")
elif marks >= 60 and marks <= 74:
    print("grade C")
elif marks >= 40 and marks <= 59:
    print("grade D")
elif marks < 40 and marks >= 0:
    print("You are failed")
else:
    print("Number is invalid")