# Write a function called discount_price that takes original_price and discount_percent as parameters and prints the final price after discount

def discount_price(original_price, discount_percent):
    discount_amt = original_price * (discount_percent / 100)
    final_amt = original_price - discount_amt
    print(f"Your final amount is {final_amt} after {discount_percent} %")

o = int(input("enter original price: "))
d = int(input("enter total discount %: "))

discount_price(o, d)