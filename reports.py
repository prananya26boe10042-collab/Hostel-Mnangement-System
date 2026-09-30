from storage import load_data
from fees import calculate_fee_status


def build_summary(data):
    total_students = len(data["students"])
    total_rooms = len(data["rooms"])

    occupied_rooms = sum(
        1 for room in data["rooms"]
        if len(room["occupants"]) > 0
    )

    available_beds = sum(
        room["capacity"] - len(room["occupants"])
        for room in data["rooms"]
    )

    fully_paid = 0
    pending_fee_students = 0
    total_collected = 0.0
    total_pending = 0.0

    for student in data["students"]:
        pending, status = calculate_fee_status(student)

        total_collected += student["fee_paid"]
        total_pending += pending

        if status == "PAID":
            fully_paid += 1
        else:
            pending_fee_students += 1

    open_complaints = sum(
        1 for complaint in data["complaints"]
        if complaint["status"] == "Open"
    )

    return {
        "total_students": total_students,
        "total_rooms": total_rooms,
        "occupied_rooms": occupied_rooms,
        "available_beds": available_beds,
        "fully_paid": fully_paid,
        "pending_fee_students": pending_fee_students,
        "total_collected": total_collected,
        "total_pending": total_pending,
        "open_complaints": open_complaints
    }


def hostel_summary():
    data = load_data()
    summary = build_summary(data)

    print("\n==============================")
    print("        HOSTEL SUMMARY")
    print("==============================")
    print("Total Students       :", summary["total_students"])
    print("Total Rooms          :", summary["total_rooms"])
    print("Occupied Rooms       :", summary["occupied_rooms"])
    print("Available Beds       :", summary["available_beds"])
    print("Students Fee Paid    :", summary["fully_paid"])
    print("Students Fee Pending :", summary["pending_fee_students"])
    print(f"Total Fee Collected  : {summary['total_collected']:.2f}")
    print(f"Total Fee Pending    : {summary['total_pending']:.2f}")
    print("Open Complaints      :", summary["open_complaints"])
    print("==============================")
