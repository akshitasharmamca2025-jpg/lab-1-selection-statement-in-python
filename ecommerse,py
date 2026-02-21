cart_value = float(input("Enter cart value: "))
membership = input("Enter membership (Silver/Gold/Platinum): ")
festival = input("Is it festival season (yes/no): ")

discount = 0

# Discount based on membership
if membership == "Silver":
    discount = 10
elif membership == "Gold":
    discount = 20
elif membership == "Platinum":
    discount = 30

# Extra festival discount
if festival == "yes":
    discount = discount + 5

# Calculate discount amount
discount_amount = cart_value * discount / 100
final_amount = cart_value - discount_amount

print("Discount =", discount, "%")
print("Final payable amount =", final_amount)