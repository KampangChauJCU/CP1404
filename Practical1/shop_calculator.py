total = 0
number_items = int(input("Number of items:"))
while number_items < 0:
    print("Invalid number of items!")
    number_items = int(input("Number of items:"))
for i in range(number_items):
    price = float(input("enter price of items:"))
    total += price
if total > 100:
    total *= 0.9
print("Total price for", number_items, "items is:${:.2f}".format(total))
