from data import students, TOTAL_HOSTEL_FEE


def generate_student_id():
    number = len(students) + 1
    student_id = "H" + str(number)
    return student_id


def find_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student

    return None


def add_student():
    print("\n--- ADD STUDENT ---")

    student_id = generate_student_id()

    name = input("Enter student name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")
    gender = input("Enter gender: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "gender": gender,
        "room": "",
        "fee_paid": 0
    }

    students.append(student)

    print("\nStudent added successfully!")
    print("Your Student ID is:", student_id)
    print("Please remember this ID for other options.")


def view_students():
    print("\n--- STUDENT DETAILS ---")

    if len(students) == 0:
        print("No students have been added yet.")
        print("Choose option 1 from the main menu to add a student.")
    else:
        for student in students:
            print("\n----------------------------")
            print("Student ID :", student["id"])
            print("Name       :", student["name"])
            print("Age        :", student["age"])
            print("Course     :", student["course"])
            print("Gender     :", student["gender"])

            if student["room"] == "":
                print("Room       : Not Assigned")
            else:
                print("Room       :", student["room"])

            print("Fee Paid   :", student["fee_paid"])
            print("Fee Pending:", TOTAL_HOSTEL_FEE - student["fee_paid"])


def search_student():
    print("\n--- SEARCH STUDENT ---")

    if len(students) == 0:
        print("No students have been added yet.")
        print("Choose option 1 first.")
        return

    student_id = input("Enter Student ID (example: H1): ")

    student = find_student(student_id)

    if student == None:
        print("Student not found.")
    else:
        print("\nStudent found!")
        print("Student ID :", student["id"])
        print("Name       :", student["name"])
        print("Course     :", student["course"])

        if student["room"] == "":
            print("Room       : Not Assigned")
        else:
            print("Room       :", student["room"])

        print("Fee Paid   :", student["fee_paid"])
        print("Fee Pending:", TOTAL_HOSTEL_FEE - student["fee_paid"])
