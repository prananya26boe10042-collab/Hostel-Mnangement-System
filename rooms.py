from data import students, rooms
from students import find_student


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
