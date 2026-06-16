age = int(input("Enter your age: "))
has_certificate = input("Certificate (True/False): ").lower() == "true"

if age >= 18:
    if has_certificate:
        print("You are eligible for this job criteria")
    else:
        print("Bring a certificate")
else:
    print("You are not eligible")