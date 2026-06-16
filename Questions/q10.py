"""
How Leap Years are CalculatedUnder the widely used Gregorian calendar, 
a leap year follows these specific rules:
The 4-Year Rule: Any year divisible by 4 is a leap year.
The 100-Year Exception: However, if the year is evenly divisible by 100, it is not a leap year.
The 400-Year Rule: But, if the year is evenly divisible by 400, it is a leap year.

Examples:
2024: Divisible by 4, not 100 → Leap Year
2000: Divisible by 400 → Leap Year
1900: Divisible by 100, but not 400 → Not a Leap Year
"""

year = int(input("Enter the Year: "))

if (year %4 == 0 and year %100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year") 
else:
    print(f"{year} not a leap year")
