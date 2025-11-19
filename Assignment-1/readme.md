import datetime


print("       DAILY CALORIE TRACKER (CLI TOOL)")
print("This tool helps you log meals, calculate total and")
print("average calories, compare with your daily limit,")
print("and optionally save your session to a file.\n")


meal_names = []
calorie_values = []

num_meals = int(input("How many meals do you want to enter today? "))

print("\n--- Enter Meal Information ---")
for i in range(num_meals):
    meal = input(f"Enter meal #{i+1} name: ")
    calories = float(input(f"Enter calories for {meal}: "))

    meal_names.append(meal)
    calorie_values.append(calories)

print("\nMeals recorded successfully!\n")


total_calories = sum(calorie_values)
average_calories = total_calories / len(calorie_values)

daily_limit = float(input("Enter your daily calorie limit: "))


print("\n--- Daily Calorie Status ---")
if total_calories > daily_limit:
    status_message = "⚠️ WARNING: You exceeded your daily calorie limit!"
else:
    status_message = "✅ Great! You are within your daily calorie limit."


print("        DAILY CALORIE SUMMARY REPORT")
print("Meal Name\t\tCalories")

for meal, cal in zip(meal_names, calorie_values):
    print(f"{meal:<15}\t{cal}")

print(f"Total Calories:\t\t{total_calories}")
print(f"Average per Meal:\t{average_calories:.2f}")
print(status_message)


save = input("Do you want to save this report? (yes/no): ").lower()

if save == "yes":
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"calorie_log_{now}.txt"

    with open(filename, "w") as file:
        file.write("DAILY CALORIE TRACKER - SESSION LOG\n")
        file.write(f"Timestamp: {now}\n\n")
        file.write("Meal Name\tCalories\n")

        for meal, cal in zip(meal_names, calorie_values):
            file.write(f"{meal:<15}\t{cal}\n")

        file.write(f"Total Calories:\t{total_calories}\n")
        file.write(f"Average Calories:\t{average_calories:.2f}\n")
        file.write(f"Daily Limit:\t{daily_limit}\n")
        file.write(f"Status: {status_message}\n")

    print(f"\n📁 Session saved successfully as: {filename}\n")

else:
    print("\nReport not saved.\n")

print("Thank you for using the Daily Calorie Tracker!")
