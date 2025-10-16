students = []  
def add_student():
    stud = {
        "id": input("Enter Student ID: "),
        "name": input("Enter Student Name: "),
        "date_of_birth": input("Enter Date of Birth: "),
        "gender": input("Enter Gender: "),
        "email": input("Enter Email: "),
        "phone": input("Enter Phone Number: "),
        "address": input("Enter Address: "),
        "parentname": input("Enter Parent/Guardian Name: "),
        "parentcontact": input("Enter Parent/Guardian Contact: "),
        "class": input("Enter Class: "),
        "program": input("Enter Program: "),
    }
    students.append(stud)
    print("Student added successfully")

def display_students():
    for student in students:
        print(f"ID: {student['id']} | Name: {student['name']} | Class: {student['class']} | Program: {student['program']}")

def search_student():
    search_id = input("Enter Student id")
    for student in students:
        if student['id'] == search_id:
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Date of Birth: {student['dob']}")
            print(f"Gender: {student['gender']}")
            print(f"Email: {student['email']}")
            print(f"Phone: {student['phone']}")
            print(f"Address: {student['address']}")
            print(f"Parent/Guardian: {student['parent_name']}")
            print(f"Parent Contact: {student['parent_contact']}")
            print(f"Class: {student['admission_class']}")
            print(f"Program: {student['program']}")
            return
    print("Student not found please input a valid student id")