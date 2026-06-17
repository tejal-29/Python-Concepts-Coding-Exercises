#true or false return , if user can vote or not

def can_vote(age):
    if age >= 18:
        return True
    else:
        return False

num = int(input("Enter your age: "))
ans = can_vote(num)
print(ans)