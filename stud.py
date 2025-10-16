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
    # STUDENT MANAGEMENT SYSTEM



def add_student():
    class_name = input("Enter class name:")
    course = input("Enter course name:")
    grade = input("Enter grade:")
    student = {"Class": class_name,
               "Course": course,
               "Grade": grade
               }
    students.append(student)
    print("student record added successfully!\n")

def view_students():
    if not students:
        print("No student record found.\n")
        return
    print("\n === Student Records ===")
    for i, student in enumerate(student, start=1):
        print(f"{i}. Class:{student['Class']}, Course: {student['Course']}, Grade: {student['Grade']}")
        print()


def search_by_class():
    search_class = input("Enter class to search:")
    results = [s for s in students if s["Class"].lower() ==search_class.lower()]
    if results:
        print(f"\nStudents in class '{search_class}':")
        for student in results:
            print(f"Course:{student['Course']}, Grade: {student['Grade']}")
    else:
        print("No records found for that class.\n")

def search_by_course():
    search_course = input("Enter course to search:")
    results = [s for s in students if s["Course"].lower() == search_course.lower()]
    if results:
        print(f"\nStudents enrolled in course '{search_course}':")
        for student in results:
            print(f"Class: {student['Class']}, Grade: {student['Grade']}")
    else:
        print("No records found for that course.\n")

#  Student Grades and Assessemnt system 

grades_data = {} 
def add_grade(student_id, subjet, score ) :
    if student_id not in grades_data:
        grades_data[student_id] = {}
    grades_data[student_id][subjet] = score
    print(f"Grade added for student {student_id} in subject {subjet} with score {score}.")
def show_grades(student_id):
    if student_id in grades_data:
        print(f"Grades for student {student_id}:")
        for subject, score in grades_data[student_id].items():
            print(f"{subject}: {score}")
    else:
        print(f"No grades found for student {student_id}.")
def calculate_average(student_id):
    if student_id in grades_data:
        scores = grades_data[student_id].values()
        average = sum(scores) / len(scores)
        print(f"Average score for student {student_id}: {average:.2f}")
    else:
        print(f"No grades found for student {student_id}.")

        def generate_report_card(student_id) :
            if student_id in grades_data :
                print (show_grades (student_id))
                average = calculate_average(student_id) 
                print (f"final result :{'Done' if average >= 50 else 'Fail'}")
                print ("         ")
            else :
                print ("student not found.")
        def update_grade(student_id, subject, new_score ) :
            if student_id in grades_data and subject in grades_data[student_id]:
                old_score = grades_data[student_id][subject]
                grades_data[student_id][subject] = new_score 
                print (f"note edit :{subject} {old_score} become {new_score}")
            else :
                print ("student or subject not found .") 
        def delete_grade(student_id, subject):
            if student_id in grades_data and subject in grades_data[student_id] :
                del grades_data[student_id][subject]      
                print (f"note deleted : {subject}")
            else :
                print("unable to deleted - student or subject not found ")