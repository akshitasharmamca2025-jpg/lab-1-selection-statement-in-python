income = float(input("Enter annual income: "))
age = int(input("Enter age: "))

tax = 0

# Set exemption limit
if age >= 60:
    exemption = 300000
else:
    exemption = 250000

# Calculate taxable income
taxable_income = income - exemption

if taxable_income <= 0:
    tax = 0
elif taxable_income <= 250000:
    tax = taxable_income * 5
elif taxable_income <= 750000:
    tax = (250000 * 0.05) + (taxable_income - 250000) * 0.20
else:
    tax = (250000 * 0.05) + (500000 * 0.20) + (taxable_income - 750000) * 0.30

print("Income Tax =", tax)