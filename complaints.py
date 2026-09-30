from data import students, complaints


def add_complaint():
    print("\n--- ADD COMPLAINT ---")

    student_id = input("Enter Student ID (example: H1): ")

    student_found = None

    for student in students:
        if student["id"] == student_id:
            student_found = student
            break

    if student_found == None:
        print("Student not found.")
        return

    complaint_text = input("Enter complaint: ")

    complaint = {
        "student_id": student_id,
        "name": student_found["name"],
        "complaint": complaint_text
    }

    complaints.append(complaint)

    print("Complaint added successfully.")


def view_complaints():
    print("\n--- COMPLAINTS ---")

    if len(complaints) == 0:
        print("No complaints found.")
    else:
        for complaint in complaints:
            print("\n----------------------------")
            print("Student ID:", complaint["student_id"])
            print("Name      :", complaint["name"])
            print("Complaint :", complaint["complaint"])
