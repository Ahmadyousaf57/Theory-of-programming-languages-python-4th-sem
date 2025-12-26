# Python Program: Online Shopping System (All Core Topics)

import math                     # Python Modules
import datetime                 # Working with Dates
import json                     # JSON handling

# 1. Comments - Explaining the purpose of the code
# This program simulates a basic online shopping system.

# 2. Variables
user_name = "Alice"
balance = 500.0

# 3. Data Types
product_name = "Laptop"
quantity = 2
price = 150.75
in_stock = True

# 4. Casting
price_int = int(price)          # Casting float to int

# 5. Strings
welcome_message = f"Welcome, {user_name}!"

# 6. Booleans
can_buy = balance >= (price * quantity)

# 7. Operators
final_price = price * quantity if can_buy else 0

# 8. Lists
cart = ["Laptop", "Mouse"]
cart.append("Keyboard")

# 9. Tuples
categories = ("Electronics", "Accessories", "Office")

# 10. Sets
payment_methods = {"Card", "UPI", "PayPal"}
payment_methods.add("Cash")

# 11. Dictionaries
products = {
    "Laptop": {"price": 150.75, "stock": 5},
    "Mouse": {"price": 20.5, "stock": 10},
}

# 12. If...Else
if can_buy:
    purchase_status = "Purchase successful!"
else:
    purchase_status = "Not enough balance."

# 13. While Loops
stock_count = 3
while stock_count > 0:
    print("Packing item...")
    stock_count -= 1

# 14. For Loops
print("Items in cart:")
for item in cart:
    print("-", item)

# 15. Functions
def calculate_total(price, qty):
    return round(price * qty, 2)

# 16. Lambda
discount = lambda p: p * 0.9
discounted_price = discount(price)

# 17. Arrays (using lists)
items_array = [10, 20, 30]

# 18. Classes/Objects
class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show_balance(self):
        return f"{self.name} has ${self.balance}"

# 19. Inheritance
class PremiumUser(User):
    def get_discount(self):
        return "20% off"

premium = PremiumUser("Alice", 500)

# 20. Iterators
items = ["Laptop", "Mouse"]
item_iter = iter(items)
print("First item:", next(item_iter))

# 21. Polymorphism
class Payment:
    def pay(self):
        return "Payment done"

class PayPal(Payment):
    def pay(self):
        return "Paid with PayPal"

def make_payment(payment_method):
    print(payment_method.pay())

make_payment(PayPal())

# 22. Scope
def outer_func():
    msg = "Outer"
    def inner_func():
        print("Accessing:", msg)
    inner_func()

outer_func()

# 23. Modules - datetime, math
print("Today’s date:", datetime.datetime.now().strftime("%Y-%m-%d"))
print("Rounded price:", math.ceil(price))

# 24. JSON
order = {
    "user": user_name,
    "items": cart,
    "total": final_price
}
order_json = json.dumps(order)
print("Order JSON:", order_json)

# 25. Try...Except
try:
    delivery_days = 5 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

# 26. User Input (mocked for example)
user_feedback = "yes"  # input("Are you satisfied with your purchase? ")

# 27. String Formatting
print("Thank you {}, your final bill is ${}".format(user_name, final_price))

