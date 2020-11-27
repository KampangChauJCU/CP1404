"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Answer: ValueError occurs when the user inputs something other than an integer.
2. When will a ZeroDivisionError occur?
Answer: ZeroDivisionError occurs when the user inputs a denominator of 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Answer: Yes, look at the code below.
"""

valid_input = False
while not valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = 0
        while denominator == 0:
            denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
print("Finished.")
