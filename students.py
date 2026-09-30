from storage import load_data, save_data
from utils import get_non_empty, get_positive_int, get_positive_float, find_student


def add_student():
    data = load_data()

    print("\n--- ADD STUDENT ---")

    student_id = get_non_empty("Enter student ID: ")

    if find_student(data["students"], student_id):
        print("A student with this ID already exists.")
        return

    name = get_non_empty("Enter student name: ")
    age = get_positive_int("Enter age: ")
    course = get_non_empty("Enter course: ")
    phone = get_non_empty("Enter phone number: ")
    total_fee = get_positive_float("Enter total hostel fee: ")

    student = {
        "student_id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "phone": phone,
        "room_no": None,
        "total_fee": total_fee,
        "fee_paid": 0.0
    }

    data["students"].append(student)
    save_data(data)

    print("Student added successfully.")


def view_students():
    data = load_data()
    students = data["students"]

    print("\n--- STUDENT LIST ---")

    if not students:
        print("No students found.")
        return

    print(f"{'ID':<12}{'Name':<22}{'Course':<20}{'Room':<12}{'Fee Paid':>12}")
    print("-" * 78)

    for student in students:
        room = student["room_no"] if student["room_no"] else "Not Assigned"
        print(
            f"{student['student_id']:<12}"
            f"{student['name']:<22}"
            f"{student['course']:<20}"
            f"{room:<12}"
            f"{student['fee_paid']:>12.2f}"
        )


def search_student():
    data = load_data()

    print("\n--- SEARCH STUDENT ---")
    student_id = get_non_empty("Enter student ID: ")

    student = find_student(data["students"], student_id)

    if not student:
        print("Student not found.")
        return

    pending_fee = max(student["total_fee"] - student["fee_paid"], 0)

    print("\nStudent Details")
    print("----------------")
    print("Student ID :", student["student_id"])
    print("Name       :", student["name"])
    print("Age        :", student["age"])
    print("Course     :", student["course"])
    print("Phone      :", student["phone"])
    print("Room       :", student["room_no"] if student["room_no"] else "Not Assigned")
    print(f"Total Fee  : {student['total_fee']:.2f}")
    print(f"Fee Paid   : {student['fee_paid']:.2f}")
    print(f"Fee Pending: {pending_fee:.2f}")
