units = int(input("Enter units consumed: "))
age = int(input("Enter age: "))

# Calculate bill
if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = units * 7
else:
    bill = units * 10

# Senior citizen discount
if age >= 60:
    discount = bill * 0.10
    bill = bill - discount

print("Electricity Bill =", bill)