from data import students, TOTAL_HOSTEL_FEE
from students import find_student


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
