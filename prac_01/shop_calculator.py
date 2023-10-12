"""
Shop Calculator
get number of items
for i, get price
if total price is greater than $100,
    apply 10% discount
print total price for number_of_items is $ total_price
"""

total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price = total_price + price
if total_price > 100:
    total_price = total_price * 0.9  # applies 10% discount
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
