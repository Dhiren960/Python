import csv
import statistics

def calculate_average(marks):
    return sum(marks.values()) / len(marks)

def calculate_median(marks):
    return statistics.median(list(marks.values()))

def find_max_score(marks):
    return max(marks.values())

def find_min_score(marks):
    return min(marks.values())

def assign_grades(marks):
    grades = {}
    for name, score in marks.items():
        if score >= 90:
            grades[name] = "A"
        elif score >= 80:
            grades[name] = "B"
        elif score >= 70:
            grades[name] = "C"
        elif score >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"
    return grades

print("GRADEBOOK ANALYZER CLI")
print("1. Manual Entry")
print("2. Load from CSV")

choice = input("Choose option (1/2): ")
marks = {}

if choice == "1":
    n = int(input("Enter number of students: "))
    for i in range(n):
        name = input("Enter name: ")
        score = int(input("Enter marks: "))
        marks[name] = score
elif choice == "2":
    filename = input("Enter CSV filename: ")
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            marks[row[0]] = int(row[1])
else:
    print("Invalid Choice")
    exit()

avg = calculate_average(marks)
med = calculate_median(marks)
mx = find_max_score(marks)
mn = find_min_score(marks)

print("\nSTATISTICAL SUMMARY")
print("Average:", avg)
print("Median:", med)
print("Max:", mx)
print("Min:", mn)

grades = assign_grades(marks)
grade_count = {"A":0,"B":0,"C":0,"D":0,"F":0}
for g in grades.values():
    grade_count[g] += 1

print("\nGRADE DISTRIBUTION")
for k,v in grade_count.items():
    print(k, ":", v)

passed_students = [name for name,score in marks.items() if score >= 40]
failed_students = [name for name,score in marks.items() if score < 40]

print("\nPassed Students:", passed_students)
print("Failed Students:", failed_students)

print("\nName\tMarks\tGrade")
print("-----------------------------")
for name in marks:
    print(f"{name}\t{marks[name]}\t{grades[name]}")

print("\nProgram Finished ✅")