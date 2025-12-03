# Title: DAILY CALORIE TRACKER 
# Nmae: Anshika Shrivastava
# Description: A The Daily Calorie Tracker is a simple tool that helps you quickly record what you ate, check your total calories, and see if you're staying within your daily limit.


print("====================================")
print("        Daily Calorie Tracker       ")
print("====================================\n")

print("This program helps you track meals and calorie intake.\n")




meal_names = []
calorie_values = []

meal_count = int(input("How many meals did you eat today? "))

for i in range(meal_count):
    print(f"\nMeal {i + 1}")
    meal = input("Enter meal name: ")
    calories = float(input("Enter calories for this meal: "))

    meal_names.append(meal)
    calorie_values.append(calories)

print("\nMeals saved successfully!\n")




total_calories = sum(calorie_values)
average_calories = total_calories / len(calorie_values)




daily_limit = float(input("Enter your daily calorie limit: "))

limit_status = (
    "You are within your daily calorie limit."
    if total_calories <= daily_limit
    else "Warning! You exceeded your daily calorie limit."
)




print("\n====================================")
print("            CALORIE REPORT          ")
print("====================================")

print(f"{'Meal':20} | Calories")
print("------------------------------------")

for i in range(len(meal_names)):
    print(f"{meal_names[i]:20} | {calorie_values[i]}")

print("------------------------------------")
print(f"{'Total Calories':20} | {total_calories}")
print(f"{'Average Calories':20} | {average_calories:.2f}\n")

print(limit_status)
print("====================================\n")




save = input("Would you like to save this report to a file? (yes/no): ").lower()

if save == "yes":
    with open("calorie_report.txt", "w") as file:
        file.write("Daily Calorie Tracker Report\n")
        file.write("====================================\n")
        file.write(f"{'Meal':20} | Calories\n")
        file.write("------------------------------------\n")

        for i in range(len(meal_names)):
            file.write(f"{meal_names[i]:20} | {calorie_values[i]}\n")

        file.write("------------------------------------\n")
        file.write(f"{'Total Calories':20} | {total_calories}\n")
        file.write(f"{'Average Calories':20} | {average_calories:.2f}\n")
        file.write(limit_status + "\n")

    print("\nReport saved successfully as 'calorie_report.txt'!")

else:
    print("\nReport not saved.")

print("\nThank you for using the Calorie Tracker!")
