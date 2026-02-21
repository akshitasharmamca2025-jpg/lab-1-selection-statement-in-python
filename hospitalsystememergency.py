age = int(input("Enter patient age: "))
heart_rate = int(input("Enter heart rate: "))
severe_injury = input("Severe injury? (yes/no): ")

# Check condition
if heart_rate < 60 or heart_rate > 100 or severe_injury == "yes":
    condition = "Critical"

elif age > 65:
    condition = "Moderate (Upgraded Priority)"

else:
    condition = "Normal"

print("Patient condition:", condition)