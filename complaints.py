from data import students, complaints
from students import find_student


def add_complaint():
    print("\n--- ADD COMPLAINT ---")

    if len(students) == 0:
        print("No students have been added yet.")
        return

    student_id = input("Enter Student ID (example: H1): ")

    student = find_student(student_id)

    if student == None:
        print("Student not found.")
        return

    message = input("Enter your complaint: ")

    complaint = {
        "student_id": student_id,
        "name": student["name"],
        "message": message
    }

    complaints.append(complaint)

    print("Complaint registered successfully.")


def view_complaints():
    print("\n--- COMPLAINTS ---")

    if len(complaints) == 0:
        print("No complaints have been registered.")
    else:
        for complaint in complaints:
            print("\n----------------------------")
            print("Student ID:", complaint["student_id"])
            print("Name      :", complaint["name"])
            print("Complaint :", complaint["message"])
