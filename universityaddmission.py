percentage = float(input("Enter 12th percentage: "))
maths = input("Did you study Mathematics (yes/no): ")
entrance_score = int(input("Enter entrance exam score: "))

if percentage < 75:
    print("Not eligible: Percentage is less than 75%")

elif maths != "yes":
    print("Not eligible: Mathematics is required")

elif entrance_score < 80:
    print("Not eligible: Entrance exam score is less than 80")

else:
    print("Eligible for admission")