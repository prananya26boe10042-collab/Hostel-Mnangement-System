# HOSTEL MANAGEMENT SYSTEM
# Beginner Python project

students = []
complaints = []

rooms = {
    "101": {"type": "Single", "capacity": 1, "students": []},
    "102": {"type": "Double", "capacity": 2, "students": []},
    "103": {"type": "Double", "capacity": 2, "students": []},
    "104": {"type": "Triple", "capacity": 3, "students": []}
}

TOTAL_HOSTEL_FEE = 50000


def show_instructions():
    print("\n====================================")
    print("      HOSTEL MANAGEMENT SYSTEM")
    print("====================================")
    print("Welcome!")
    print("If you are using the system for the first time,")
    print("choose option 1 to add a student.")
    print("The system will create a Student ID automatically.")
    print("Use that Student ID for room, fee and complaint options.")


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


def view_rooms():
    print("\n--- ROOM STATUS ---")

    for room_number in rooms:
        room = rooms[room_number]

        occupied = len(room["students"])
        available = room["capacity"] - occupied

        print("\nRoom Number:", room_number)
        print("Room Type  :", room["type"])
        print("Capacity   :", room["capacity"])
        print("Occupied   :", occupied)
        print("Available  :", available)


def assign_room():
    print("\n--- ASSIGN ROOM ---")

    if len(students) == 0:
        print("No students have been added yet.")
        print("Choose option 1 first.")
        return

    student_id = input("Enter Student ID (example: H1): ")

    student = find_student(student_id)

    if student == None:
        print("Student not found.")
        return

    if student["room"] != "":
        print("This student already has room", student["room"])
        return

    print("\nAvailable room details:")
    view_rooms()

    room_number = input("\nEnter room number: ")

    if room_number not in rooms:
        print("Invalid room number.")
        return

    room = rooms[room_number]

    if len(room["students"]) >= room["capacity"]:
        print("Sorry, this room is full.")
    else:
        room["students"].append(student_id)
        student["room"] = room_number

        print("Room", room_number, "assigned successfully to", student["name"])


def vacate_room():
    print("\n--- VACATE ROOM ---")

    if len(students) == 0:
        print("No students have been added yet.")
        return

    student_id = input("Enter Student ID (example: H1): ")

    student = find_student(student_id)

    if student == None:
        print("Student not found.")
        return

    if student["room"] == "":
        print("This student does not have a room assigned.")
    else:
        room_number = student["room"]

        rooms[room_number]["students"].remove(student_id)
        student["room"] = ""

        print("Room", room_number, "vacated successfully.")


def pay_fee():
    print("\n--- HOSTEL FEE PAYMENT ---")

    if len(students) == 0:
        print("No students have been added yet.")
        return

    student_id = input("Enter Student ID (example: H1): ")

    student = find_student(student_id)

    if student == None:
        print("Student not found.")
        return

    pending_fee = TOTAL_HOSTEL_FEE - student["fee_paid"]

    print("Total Hostel Fee:", TOTAL_HOSTEL_FEE)
    print("Already Paid    :", student["fee_paid"])
    print("Pending Fee     :", pending_fee)

    if pending_fee == 0:
        print("The hostel fee is already fully paid.")
        return

    amount = input("Enter amount to pay: ")

    if amount.isdigit():
        amount = int(amount)

        if amount <= 0:
            print("Please enter an amount greater than 0.")
        elif amount > pending_fee:
            print("Amount is more than the pending fee.")
        else:
            student["fee_paid"] = student["fee_paid"] + amount

            print("Payment recorded successfully.")
            print("Total Fee Paid:", student["fee_paid"])
            print("Fee Pending   :", TOTAL_HOSTEL_FEE - student["fee_paid"])
    else:
        print("Please enter the amount using numbers only.")


def view_fee_status():
    print("\n--- FEE STATUS ---")

    if len(students) == 0:
        print("No students have been added yet.")
        return

    for student in students:
        pending_fee = TOTAL_HOSTEL_FEE - student["fee_paid"]

        print("\n----------------------------")
        print("Student ID :", student["id"])
        print("Name       :", student["name"])
        print("Total Fee  :", TOTAL_HOSTEL_FEE)
        print("Fee Paid   :", student["fee_paid"])
        print("Fee Pending:", pending_fee)

        if pending_fee == 0:
            print("Status     : Fully Paid")
        elif student["fee_paid"] == 0:
            print("Status     : Not Paid")
        else:
            print("Status     : Partially Paid")


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


def hostel_summary():
    print("\n--- HOSTEL SUMMARY ---")

    total_students = len(students)
    total_beds = 0
    occupied_beds = 0
    total_fee_collected = 0

    for room_number in rooms:
        total_beds = total_beds + rooms[room_number]["capacity"]
        occupied_beds = occupied_beds + len(rooms[room_number]["students"])

    for student in students:
        total_fee_collected = total_fee_collected + student["fee_paid"]

    available_beds = total_beds - occupied_beds

    print("Total Students      :", total_students)
    print("Total Beds          :", total_beds)
    print("Occupied Beds       :", occupied_beds)
    print("Available Beds      :", available_beds)
    print("Total Fee Collected :", total_fee_collected)
    print("Total Complaints    :", len(complaints))


def main():
    show_instructions()

    choice = ""

    while choice != "0":
        print("\n====================================")
        print("             MAIN MENU")
        print("====================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Assign Room")
        print("5. Vacate Room")
        print("6. View Room Status")
        print("7. Pay Hostel Fee")
        print("8. View Fee Status")
        print("9. Add Complaint")
        print("10. View Complaints")
        print("11. Hostel Summary")
        print("0. Exit")

        choice = input("\nEnter your choice from 0 to 11: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            assign_room()

        elif choice == "5":
            vacate_room()

        elif choice == "6":
            view_rooms()

        elif choice == "7":
            pay_fee()

        elif choice == "8":
            view_fee_status()

        elif choice == "9":
            add_complaint()

        elif choice == "10":
            view_complaints()

        elif choice == "11":
            hostel_summary()

        elif choice == "0":
            print("\nThank you for using the Hostel Management System.")

        else:
            print("Invalid choice. Please enter a number from 0 to 11.")


main()
