from datetime import datetime

from storage import load_data, save_data
from utils import get_non_empty, get_positive_float, find_student


def calculate_fee_status(student):
    pending = max(student["total_fee"] - student["fee_paid"], 0)

    if pending == 0:
        status = "PAID"
    elif student["fee_paid"] > 0:
        status = "PARTIALLY PAID"
    else:
        status = "PENDING"

    return pending, status


def pay_hostel_fee():
    data = load_data()

    print("\n--- PAY HOSTEL FEE ---")

    student_id = get_non_empty("Enter student ID: ")
    student = find_student(data["students"], student_id)

    if not student:
        print("Student not found.")
        return

    pending, status = calculate_fee_status(student)

    if pending == 0:
        print("This student's hostel fee is already fully paid.")
        return

    print(f"Current fee status: {status}")
    print(f"Pending amount    : {pending:.2f}")

    amount = get_positive_float("Enter payment amount: ")

    if amount > pending:
        print("Payment cannot be greater than the pending amount.")
        return

    student["fee_paid"] += amount

    data["payments"].append({
        "student_id": student["student_id"],
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    save_data(data)

    new_pending, new_status = calculate_fee_status(student)

    print("Payment recorded successfully.")
    print(f"New fee status: {new_status}")
    print(f"Pending amount : {new_pending:.2f}")


def view_fee_status():
    data = load_data()

    print("\n--- FEE STATUS ---")

    if not data["students"]:
        print("No students found.")
        return

    print(
        f"{'ID':<12}"
        f"{'Name':<22}"
        f"{'Total Fee':>12}"
        f"{'Paid':>12}"
        f"{'Pending':>12}"
        f"{'Status':>18}"
    )
    print("-" * 88)

    for student in data["students"]:
        pending, status = calculate_fee_status(student)

        print(
            f"{student['student_id']:<12}"
            f"{student['name']:<22}"
            f"{student['total_fee']:>12.2f}"
            f"{student['fee_paid']:>12.2f}"
            f"{pending:>12.2f}"
            f"{status:>18}"
        )
