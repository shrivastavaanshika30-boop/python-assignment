  
# Title: Gradebook Analyzer
# Nmae: Anshika Shrivastava
# Description: A complete gradebook analyzer that allows users
#              to input student marks manually or from CSV,
#              perform statistical analysis, assign grades,
#              and display formatted results.
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import csv

def manual_entry():
    """Manual entry of student names and marks."""
    marks = {}
    print("\n Manual Data Entry Mode")
    print("Enter student names and marks. Type 'done' to finish.\n")

    while True:
        name = input("Enter student name (or 'done' to finish): ").strip()
        if name.lower() == "done":
            break
        score = float(input(f"Enter marks for {name}: "))
        marks[name] = score
    return marks


def load_from_csv():
    """Load student names and marks from a CSV file."""
    marks = {}
    print("\n📂 CSV Import Mode")
    file_path = input("Enter CSV file path (e.g., data.csv): ").strip()

    file = open(file_path, mode='r')
    reader = csv.DictReader(file)
    for row in reader:
        name = row["Name"]
        mark = float(row["Marks"])
        marks[name] = mark
    file.close()
    return marks



def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict) if marks_dict else 0


def calculate_median(marks_dict):
    sorted_marks = sorted(marks_dict.values())
    n = len(sorted_marks)
    if n == 0:
        return 0
    mid = n // 2
    if n % 2 == 0:
        return (sorted_marks[mid - 1] + sorted_marks[mid]) / 2
    else:
        return sorted_marks[mid]


def find_max_score(marks_dict):
    return max(marks_dict.values()) if marks_dict else 0


def find_min_score(marks_dict):
    return min(marks_dict.values()) if marks_dict else 0


def assign_grades(marks_dict):
    grades = {}
    for name, score in marks_dict.items():
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        grades[name] = grade
    return grades


def grade_distribution(grades_dict):
    counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for grade in grades_dict.values():
        counts[grade] += 1
    return counts


def pass_fail_lists(marks_dict):
    passed_students = [name for name, mark in marks_dict.items() if mark >= 40]
    failed_students = [name for name, mark in marks_dict.items() if mark < 40]
    return passed_students, failed_students


def display_results_table(marks_dict, grades_dict):
    print("\n=============================================")
    print("Name\t\tMarks\tGrade")
    print("---------------------------------------------")
    for name, score in marks_dict.items():
        print(f"{name:<15}\t{score:<7}\t{grades_dict[name]}")
    print("=============================================")


def main():
    while True:
        print("\n==========================================")
        print("    Welcome to the Gradebook Analyzer!  ")
        print("==========================================\n")
        print("1. Enter student data manually")
        print("2. Load student data from a CSV file")
        print("3. Exit")

        choice = input("\nEnter your choice (1/2/3): ")

        if choice == "3":
            print("\n Exiting the Gradebook Analyzer. Goodbye!")
            break

        # Step 1: Data Entry
        if choice == "1":
            marks = manual_entry()
        elif choice == "2":
            marks = load_from_csv()
        else:
            print(" Invalid choice. Please enter 1, 2, or 3.")
            continue

        # Step 2: Statistical Analysis
        avg = calculate_average(marks)
        median = calculate_median(marks)
        max_score = find_max_score(marks)
        min_score = find_min_score(marks)

        print("\n Statistical Summary:")
        print(f"Average Marks: {avg:.2f}")
        print(f"Median Marks:  {median:.2f}")
        print(f"Highest Marks: {max_score}")
        print(f"Lowest Marks:  {min_score}")

        # Step 3: Grade Assignment
        grades = assign_grades(marks)
        dist = grade_distribution(grades)

        # Step 4: Pass/Fail Filter
        passed, failed = pass_fail_lists(marks)

        # Step 5: Display Results Table
        display_results_table(marks, grades)

        print("\n Grade Distribution:")
        for g, count in dist.items():
            print(f"Grade {g}: {count} student(s)")

        print(f"\n Passed: {len(passed)} students → {passed}")
        print(f"Failed: {len(failed)} students → {failed}")

        # Step 6: Repeat Option
        again = input("\nWould you like to analyze another dataset? (y/n): ").lower()
        if again != "y":
            print("\n Thank you for using the Gradebook Analyzer!")
            break


if __name__ == "__main__":
    main()
