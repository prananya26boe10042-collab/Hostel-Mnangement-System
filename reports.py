from data import students, complaints, rooms


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
