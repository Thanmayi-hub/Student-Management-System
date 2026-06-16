students = []
# Add Student
def add_student():
    name = input("Enter name: ")
    dept = input("Enter department: ")
    phone = input("Enter phone: ")
    cgpa = input("Enter CGPA: ")
    student = {
        "name": name,
        "department": dept,
        "phone": phone,
        "cgpa": cgpa
    }
    students.append(student)
    print("Student added successfully!")
# View Students
def view_students():
    if len(students) == 0:
        print("No students found")
    else:
        print("\n--- Student List ---")
        for s in students:
            print(f"Name: {s['name']}, Dept: {s['department']}, Phone: {s['phone']}, CGPA: {s['cgpa']}")
# Search Student
def search_student():
    name = input("Enter name to search: ")
    for s in students:
        if s["name"].lower() == name.lower():
            print("Student Found:")
            print(s)
            return
    print("Student not found")
# Update Student
def update_student():
    name = input("Enter name to update: ")

    for s in students:
        if s["name"].lower() == name.lower():
            print("Enter new details (leave blank to keep old value):")

            new_dept = input("New department: ")
            new_phone = input("New phone: ")
            new_cgpa = input("New CGPA: ")

            if new_dept:
                s["department"] = new_dept
            if new_phone:
                s["phone"] = new_phone
            if new_cgpa:
                s["cgpa"] = new_cgpa

            print("Student updated successfully!")
            return

    print("Student not found")
# Delete Student
def delete_student():
    name = input("Enter name to delete: ")
    for s in students:
        if s["name"].lower() == name.lower():
            students.remove(s)
            print("Student deleted successfully!")
            return

    print("Student not found")
# Menu System
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_student()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        print("Exiting program... Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
