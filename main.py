from storage import initialize_storage
from students import add_student, view_students, search_student
from rooms import assign_room, vacate_room, view_room_status
from fees import pay_hostel_fee, view_fee_status
from complaints import add_complaint, view_complaints
from reports import hostel_summary


def print_menu():
    print("\n==============================")
    print("   HOSTEL MANAGEMENT SYSTEM")
    print("==============================")
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


def main():
    initialize_storage()

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

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
            view_room_status()

        elif choice == "7":
            pay_hostel_fee()

        elif choice == "8":
            view_fee_status()

        elif choice == "9":
            add_complaint()

        elif choice == "10":
            view_complaints()

        elif choice == "11":
            hostel_summary()

        elif choice == "0":
            print("Program closed. Thank you.")
            break

        else:
            print("Invalid choice. Please enter a number from 0 to 11.")


if __name__ == "__main__":
    main()
