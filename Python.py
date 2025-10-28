# Student Management System (Simple CRUD Project)
# Author: Sukanya Sonawane
# Language: Python 3

students = {}  # Dictionary to store student data

def add_student():
    roll_no = input("Enter Roll Number: ")
    if roll_no in students:
        print("Student already exists!\n")
        return
    name = input("Enter Student Name: ")
    course = input("Enter Course Name: ")
    marks = input("Enter Marks: ")
    students[roll_no] = {"name": name, "course": course, "marks": marks}
    print("✅ Student added successfully!\n")

def display_students():
    if not students:
        print("No records found!\n")
        return
    print("\n--- Student Records ---")
    for roll_no, info in students.items():
        print(f"Roll No: {roll_no}")
        print(f"Name: {info['name']}")
        print(f"Course: {info['course']}")
        print(f"Marks: {info['marks']}")
        print("------------------------")
    print()

def update_student():
    roll_no = input("Enter Roll Number to Update: ")
    if roll_no not in students:
        print("Student not found!\n")
        return
    print("Enter new details (leave blank to keep old value):")
    name = input(f"Name ({students[roll_no]['name']}): ") or students[roll_no]['name']
    course = input(f"Course ({students[roll_no]['course']}): ") or students[roll_no]['course']
    marks = input(f"Marks ({students[roll_no]['marks']}): ") or students[roll_no]['marks']
    students[roll_no] = {"name": name, "course": course, "marks": marks}
    print("✅ Student updated successfully!\n")

def delete_student():
    roll_no = input("Enter Roll Number to Delete: ")
    if roll_no in students:
        del students[roll_no]
        print("🗑️ Student deleted successfully!\n")
    else:
        print("Student not found!\n")

def search_student():
    roll_no = input("Enter Roll Number to Search: ")
    if roll_no in students:
        info = students[roll_no]
        print("\n--- Student Found ---")
        print(f"Roll No: {roll_no}")
        print(f"Name: {info['name']}")
        print(f"Course: {info['course']}")
        print(f"Marks: {info['marks']}\n")
    else:
        print("Student not found!\n")

def menu():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            search_student()
        elif choice == '6':
            print("👋 Exiting the program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

# Run the program
menu()
