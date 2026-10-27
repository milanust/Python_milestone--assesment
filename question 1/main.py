# Student Marks Management System

def calculate_grade(avg):
    if avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "F"


def display_student(student):
    print("\nStudent ID:", student["id"])
    print("Name:", student["name"])
    print("Total:", student["total"])
    print("Average:", round(student["average"], 2))
    print("Grade:", student["grade"])
    print("Result:", student["result"])


students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details for Student {i + 1}")

    student_id = input("Student ID: ")
    name = input("Student Name: ")

    python_marks = float(input("Python Marks: "))
    sql_marks = float(input("SQL Marks: "))
    ai_marks = float(input("AI Marks: "))

    total = python_marks + sql_marks + ai_marks
    average = total / 3

    grade = calculate_grade(average)

    result = "PASS" if average >= 40 else "FAIL"

    student = {
        "id": student_id,
        "name": name,
        "python": python_marks,
        "sql": sql_marks,
        "ai": ai_marks,
        "total": total,
        "average": average,
        "grade": grade,
        "result": result
    }

    students.append(student)

print("\n======= STUDENT RESULTS =======")

for student in students:
    display_student(student)

# Highest Average Student
highest_student = max(students, key=lambda x: x["average"])

print("\nHighest Scoring Student:", highest_student["name"])

# List Comprehension
students_above_75 = [
    student["name"]
    for student in students
    if student["average"] > 75
]

print("Students above 75 Average:",
      ", ".join(students_above_75) if students_above_75 else "None")