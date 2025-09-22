"""
writing a shop calculator, getting the user to input number of items
"""
# Asking user to input number of items
number_of_items = int(input('Enter the number of items: '))
total_price = 0
# Checking if there is an invalid input
while number_of_items < 0:
    print('invalid')
    number_of_items = int(input('Enter the number of items: '))
# for loop adding the cost to the total number of items
for i in range(number_of_items):
    item_price = float(input('Enter the item price: '))
    total_price += item_price
# writing an if statement to check the conditions to apply a discount if eligible
# else to print the regular price without discount
if total_price > 100:
    total_price *= 0.9
    print(f"Your Total price after 10% discount is: {total_price}, thank you for shopping with us!")
else:
    print(f"Your Total price is: {total_price}, thank you for shopping with us!")