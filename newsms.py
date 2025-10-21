# STUDENT INFORMATION (NANA YAW)
students = []

def add_student():
    """Add a new student record"""
    stud = {
        "id": input("Enter Student ID: "),
        "name": input("Enter Student Name: "),
        "date_of_birth": input("Enter Date of Birth (YYYY-MM-DD): "),
        "gender": input("Enter Gender: "),
        "email": input("Enter Email: "),
        "phone": input("Enter Phone Number: "),
        "address": input("Enter Address: "),
        "parentname": input("Enter Parent/Guardian Name: "),
        "parentcontact": input("Enter Parent/Guardian Contact: "),
        "class": input("Enter Class: "),
        "program": input("Enter Program: ")
    }
    students.append(stud)
    print("\n✅ Student added successfully!\n")


def display_students():
    """Display all student records"""
    if not students:
        print("\nNo students available.\n")
        return
    print("\n=== STUDENT LIST ===")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | Class: {s['class']} | Program: {s['program']}")
    print()


def search_student():
    """Search for a student by ID"""
    search_id = input("Enter Student ID to search: ")
    for s in students:
        if s['id'] == search_id:
            print("\n=== STUDENT DETAILS ===")
            for key, value in s.items():
                print(f"{key.title()}: {value}")
            print()
            return
    print("\nStudent not found.\n")


def view_students():
    """View all student details"""
    if not students:
        print("\nNo student record found.\n")
        return
    print("\n=== Student Records ===")
    for i, student in enumerate(students, start=1):
        print(f"{i}. ID: {student['id']} | Name: {student['name']} | Class: {student['class']} | Program: {student['program']}")
    print()


# Mr Ibrahim Section
def search_by_class():
    """Search for all students in a particular class"""
    search_class = input("Enter class to search: ")
    results = [s for s in students if s["class"].lower() == search_class.lower()]
    if results:
        print(f"\nStudents in class '{search_class}':")
        for s in results:
            print(f"ID: {s['id']} | Name: {s['name']} | Program: {s['program']}")
    else:
        print("\nNo records found for that class.\n")


def search_class_by_name():
    """Search for a student's class using their name"""
    name = input("Enter student name: ")
    for s in students:
        if s["name"].lower() == name.lower():
            print(f"\n{s['name']} is in class {s['class']}.\n")
            return
    print("\nStudent not found.\n")


# GRADES & ASSESSMENT (EMMANUEL)
grades_data = {}

def add_grade():
    """Add a grade for a student"""
    student_id = input("Enter Student ID: ")
    subject = input("Enter Subject: ")
    try:
        score = float(input("Enter Score: "))
    except ValueError:
        print("Invalid score input.")
        return
    if student_id not in grades_data:
        grades_data[student_id] = {}
    grades_data[student_id][subject] = score
    print(f"\n✅ Grade added for student {student_id}: {subject} = {score}\n")


def show_grades():
    """Display all grades for a student"""
    student_id = input("Enter Student ID: ")
    if student_id in grades_data:
        print(f"\n=== Grades for {student_id} ===")
        for subject, score in grades_data[student_id].items():
            print(f"{subject}: {score}")
        print()
    else:
        print("\nNo grades found for this student.\n")


def calculate_average():
    """Calculate and display average score"""
    student_id = input("Enter Student ID: ")
    if student_id in grades_data and grades_data[student_id]:
        scores = list(grades_data[student_id].values())
        avg = sum(scores) / len(scores)
        print(f"\nAverage score for {student_id}: {avg:.2f}")
        print(f"Result: {'PASS' if avg >= 50 else 'FAIL'}\n")
    else:
        print("\nNo grades found for this student.\n")


def update_grade():
    """Update an existing grade"""
    student_id = input("Enter Student ID: ")
    subject = input("Enter Subject: ")
    if student_id in grades_data and subject in grades_data[student_id]:
        try:
            new_score = float(input("Enter New Score: "))
        except ValueError:
            print("Invalid score input.")
            return
        old = grades_data[student_id][subject]
        grades_data[student_id][subject] = new_score
        print(f"\nUpdated {subject}: {old} → {new_score}\n")
    else:
        print("\nGrade not found.\n")


def delete_grade():
    """Delete a grade for a student"""
    student_id = input("Enter Student ID: ")
    subject = input("Enter Subject to delete: ")
    if student_id in grades_data and subject in grades_data[student_id]:
        del grades_data[student_id][subject]
        print(f"\nDeleted {subject} for {student_id}\n")
    else:
        print("\nGrade not found.\n")


# FEE MANAGEMENT (E)
students_fees = {}

def register_fee_student():
    """Register a new student for fee management"""
    sid = input("Enter Student ID: ")
    if sid in students_fees:
        print("\nStudent already exists in fee system.\n")
    else:
        name = input("Enter Student Name: ")
        program = input("Enter Program: ")
        fees_structure = input("Enter Fee Structure (Day/Boarding): ")
        try:
            fees_amount = float(input("Enter Total Fee Amount: "))
        except ValueError:
            print("Invalid amount input.")
            return
        students_fees[sid] = {
            "name": name,
            "program": program,
            "structure": fees_structure,
            "total": fees_amount,
            "paid": 0.0
        }
        print("\n✅ Student added to Fee Management successfully!\n")


def record_payment():
    """Record a payment for a student"""
    sid = input("Enter Student ID: ")
    if sid in students_fees:
        try:
            amount = float(input("Enter Payment Amount: "))
        except ValueError:
            print("Invalid payment amount.")
            return
        students_fees[sid]["paid"] += amount
        print(f"\n💰 Payment of {amount:.2f} recorded successfully.\n")
    else:
        print("\nStudent not found in Fee Management.\n")


def display_fee_records():
    """Display all student fee records"""
    if not students_fees:
        print("\nNo fee records found.\n")
        return
    print("\n=== FEE RECORDS ===")
    for sid, info in students_fees.items():
        balance = info["total"] - info["paid"]
        print(f"ID: {sid} | Name: {info['name']} | Paid: {info['paid']:.2f} | Balance: {balance:.2f}")
    print()


# MAIN MENU (NHYIRA - GROUP LEADER)
def main_menu():
    while True:
        print("""
======== STUDENT MANAGEMENT SYSTEM ========
1. Add Student
2. Display Students
3. Search Student by ID
4. View All Students
5. Search Students by Class
6. Search Student's Class by Name
7. Add Grade
8. Show Grades
9. Calculate Average
10. Update Grade
11. Delete Grade
12. Register Fee Student
13. Record Fee Payment
14. Display Fee Records
0. Exit
===========================================
""")
        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            view_students()
        elif choice == "5":
            search_by_class()
        elif choice == "6":
            search_class_by_name()
        elif choice == "7":
            add_grade()
        elif choice == "8":
            show_grades()
        elif choice == "9":
            calculate_average()
        elif choice == "10":
            update_grade()
        elif choice == "11":
            delete_grade()
        elif choice == "12":
            register_fee_student()
        elif choice == "13":
            record_payment()
        elif choice == "14":
            display_fee_records()
        elif choice == "0":
            print("\n👋 Exiting... Goodbye!\n")
            break
        else:
            print("\nInvalid choice. Try again.\n")


if __name__ == "__main__":
    main_menu()
