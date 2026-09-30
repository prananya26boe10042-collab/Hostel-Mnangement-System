from storage import load_data, save_data
from utils import get_non_empty, find_student


def find_room(rooms, room_no):
    for room in rooms:
        if room["room_no"] == room_no:
            return room

    return None


def room_is_available(room):
    return len(room["occupants"]) < room["capacity"]


def assign_room():
    data = load_data()

    print("\n--- ASSIGN ROOM ---")

    student_id = get_non_empty("Enter student ID: ")
    student = find_student(data["students"], student_id)

    if not student:
        print("Student not found.")
        return

    if student["room_no"]:
        print(f"Student is already assigned to room {student['room_no']}.")
        return

    available_rooms = [
        room for room in data["rooms"]
        if room_is_available(room)
    ]

    if not available_rooms:
        print("No rooms are currently available.")
        return

    print("\nAvailable Rooms")
    for room in available_rooms:
        available_beds = room["capacity"] - len(room["occupants"])
        print(f"Room {room['room_no']} - {available_beds} bed(s) available")

    room_no = get_non_empty("Enter room number to assign: ")
    room = find_room(data["rooms"], room_no)

    if not room:
        print("Invalid room number.")
        return

    if not room_is_available(room):
        print("That room is already full.")
        return

    room["occupants"].append(student["student_id"])
    student["room_no"] = room["room_no"]

    save_data(data)

    print(f"Room {room_no} assigned successfully to {student['name']}.")


def vacate_room():
    data = load_data()

    print("\n--- VACATE ROOM ---")

    student_id = get_non_empty("Enter student ID: ")
    student = find_student(data["students"], student_id)

    if not student:
        print("Student not found.")
        return

    if not student["room_no"]:
        print("This student does not have an assigned room.")
        return

    room = find_room(data["rooms"], student["room_no"])

    if room and student["student_id"] in room["occupants"]:
        room["occupants"].remove(student["student_id"])

    old_room = student["room_no"]
    student["room_no"] = None

    save_data(data)

    print(f"Room {old_room} vacated successfully.")


def view_room_status():
    data = load_data()

    print("\n--- ROOM STATUS ---")
    print(f"{'Room':<10}{'Capacity':<12}{'Occupied':<12}{'Available':<12}{'Student IDs'}")
    print("-" * 70)

    for room in data["rooms"]:
        occupied = len(room["occupants"])
        available = room["capacity"] - occupied
        occupants = ", ".join(room["occupants"]) if room["occupants"] else "-"

        print(
            f"{room['room_no']:<10}"
            f"{room['capacity']:<12}"
            f"{occupied:<12}"
            f"{available:<12}"
            f"{occupants}"
        )
