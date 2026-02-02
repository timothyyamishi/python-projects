# =====================================================================
# STUDENT ACADEMIC RECORD MANAGEMENT SYSTEM
# =====================================================================

# Global dictionary to store student records
students = {}

# Function to determine grade based on average marks
def calculate_grade(average):
    if average >= 75:
        return "A"
    elif average >= 65:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

# Function to register a new student and their marks
def add_student():
    student_id = input("Enter Student ID: ")

    # Check for duplicate IDs
    if student_id in students:
        print("Student ID already exists.")
        return

    name = input("Enter Full Name: ")
    class_name = input("Enter Class: ")
    subjects = {}

    # Input loop for at least 3 subjects
    for i in range(3):
        subject = input(f"Enter subject {i+1} name: ")
        while True:
            try:
                mark = int(input(f"Enter marks for {subject} (0-100): "))
                if 0 <= mark <= 100:
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")
        subjects[subject] = mark

    # Store data in nested dictionary
    students[student_id] = {
        "name": name,
        "class": class_name,
        "subjects": subjects
    }
    print("Student added successfully.")

# Function to list all registered students
def view_all_students():
    if not students:
        print("No student records available.")
        return

    print("\n--- ALL STUDENTS ---")
    for student_id, details in students.items():
        print(f"ID: {student_id} | Name: {details['name']}")

# Function to display detailed report for a specific student
def view_student_report():
    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]
    subjects = student["subjects"]

    # Perform calculations
    total = sum(subjects.values())
    average = total / len(subjects)
    grade = calculate_grade(average)

    print("\n--- STUDENT REPORT ---")
    print(f"Name: {student['name']}")
    print(f"Class: {student['class']}")
    print("Subjects and Marks:")
    for subject, mark in subjects.items():
        print(f" - {subject}: {mark}")
    print(f"Total Marks: {total}")
    print(f"Average: {round(average, 2)}")
    print(f"Grade: {grade}")

# Function to modify marks for an existing subject
def update_marks():
    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found.")
        return

    subject = input("Enter subject name to update: ")
    if subject not in students[student_id]["subjects"]:
        print("Subject not found.")
        return

    while True:
        try:
            new_mark = int(input("Enter new marks (0-100): "))
            if 0 <= new_mark <= 100:
                break
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Enter a valid number.")

    students[student_id]["subjects"][subject] = new_mark
    print("Marks updated successfully.")

# Function to remove a student record
def delete_student():
    student_id = input("Enter Student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student record deleted.")
    else:
        print("Student not found.")

# Main program loop
def main_menu():
    while True:
        print("""
==============================
STUDENT MANAGEMENT MENU
==============================
1. Add Student
2. View All Students
3. View Student Report
4. Update Marks
5. Delete Student
6. Exit
""")
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            view_student_report()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Program terminated. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Entry point
if __name__ == "__main__":
    main_menu()
