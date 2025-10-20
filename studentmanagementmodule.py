#  STUDENT INFORMATION (NANA YAW)
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
    print( "Student added successfully")

def display_students():
    """Display all student records"""
    if not students:
        print(" No students available.\n")
        return
    print( "STUDENT LIST")
    for s in students:
        print(f"ID: {s['id']}Name: {s['name']}Class: {s['class']}Program: {s['program']}")
    print()

def search_student():
    """Search for a student by ID"""
    search_id = input("Enter Student ID to search: ")
    for s in students:
        if s['id'] == search_id:
            print(" STUDENT DETAILS ")
            for key, value in s.items():
                print(f"{key.title()}: {value}")
            print()
            return
    print(" Student not found ")


#  GRADES & ASSESSMENT PART(MR IBRAHIM)
grades_data = {}

def add_grade():
    """Add a grade for a student"""
    student_id = input("Enter Student ID: ")
    subject = input("Enter Subject: ")
    score = float(input("Enter Score: "))
    if student_id not in grades_data:
        grades_data[student_id] = {}
    grades_data[student_id][subject] = score
    print(f" Grade added for student {student_id}: {subject} = {score}")

def show_grades():
    """Display all grades for a student"""
    student_id = input("Enter Student ID: ")
    if student_id in grades_data:
        print(f" Grades for {student_id}:")
        for subject, score in grades_data[student_id].items():
            print(f"{subject}: {score}")
        print()
    else:
        print(" No grades found for this student.")

def calculate_average():
    """Calculate and display average score"""
    student_id = input("Enter Student ID: ")
    if student_id in grades_data:
        scores = list(grades_data[student_id].values())
        avg = sum(scores) / len(scores)
        print(f"Average score for {student_id}: {avg:.2f}")
        print(f"Result: {'PASS' if avg >= 50 else 'FAIL'}\n")
    else:
        print(" No grades found.")

def update_grade():
    """Update an existing grade"""
    student_id = input("Enter Student ID: ")
    subject = input("Enter Subject: ")
    if student_id in grades_data and subject in grades_data[student_id]:
        new_score = float(input("Enter New Score: "))
        old = grades_data[student_id][subject]
        grades_data[student_id][subject] = new_score
        print(f" Updated {subject}: {old} → {new_score}")
    else:
        print(" Grade not found.\n")

def delete_grade():
    """Delete a grade for a student"""
    student_id = input("Enter Student ID: ")
    subject = input("Enter Subject to delete: ")
    if student_id in grades_data and subject in grades_data[student_id]:
        del grades_data[student_id][subject]
        print(f" Deleted {subject} for {student_id}\n")
    else:
        print(" Grade not found.\n")

# FEE MANAGEMENT (EMMANUEL)
students_fees = {}
def register_fee_student():
    """Register a new student for fee management"""
    sid = input("Enter Student ID: ")
    if sid in students_fees:
        print(" Student already exists in fee system.")
    else:
        name = input("Enter Student Name: ")
        program = input("Enter Program: ")
        fees_structure = input("Enter Fee Structure (Day/Boarding): ")
        fees_amount = float(input("Enter Total Fee Amount: "))
        paid = 0
        students_fees[sid] = {
            "name": name,
            "program": program,
            "structure": fees_structure,
            "total": fees_amount,
            "paid": paid
        }
        print("\n Student added to Fee Management successfully!\n")

def record_payment():
    """Record a payment for a student"""
    sid = input("Enter Student ID: ")
    if sid in students_fees:
        amount = float(input("Enter Payment Amount: "))
        students_fees[sid]["paid"] += amount
        print(f" Payment of {amount:.2f} recorded successfully.")
    else:
        print(" Student not found in Fee Management.\n")

def display_fee_records():
    """Display all student fee records"""
    if not students_fees:
        print(" No fee records found.\n")
        return
    print("\n--- FEE RECORDS ---")
    for sid, info in students_fees.items():
        balance = info["total"] - info["paid"]
        print(f"ID: {sid} | Name: {info['name']} | Paid: {info['paid']} | Balance: {balance}")
    print()


#  MAIN MENU(NHYIRA(GROUP LEADER))
def main_menu():
    while True:
        print("""STUDENT MANAGEMENT SYSTEM
1. Add Student
2. Display Students
3. Search Student
4. Add Grade
5. Show Grades
6. Calculate Average
7. Update Grade
8. Delete Grade
9. Register Fee Student
10. Record Fee Payment
11. Display Fee Records
0. Exit
""")
        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            add_grade()
        elif choice == "5":
            show_grades()
        elif choice == "6":
            calculate_average()
        elif choice == "7":
            update_grade()
        elif choice == "8":
            delete_grade()
        elif choice == "9":
            view_fee_structure()
        elif choice == "10":
            record_payment()
        elif choice == "11":
            display_fee_records()
        elif choice == "0":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()