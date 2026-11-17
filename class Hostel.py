class Hostel:
    def __init__(self):
        self.rooms = {
            101: None,
            102: None,
            103: {"name": "Shobha", "roll": "101"},
            104: None,
            105: {"name": "Gaurav", "roll": "102"}
        }

    def view_rooms(self):
        print("\n--- HOSTEL ROOM DETAILS ---")
        for room, student in self.rooms.items():
            if student is None:
                print("Room", room, "- Available")
            else:
                print("Room", room, "- Occupied by", student)

    def register_student(self):
        name = input("Enter student name: ")
        roll = input("Enter student USN/Roll number: ")
        room = int(input("Enter room number: "))

        if room in self.rooms:
            if self.rooms[room] is None:
                self.rooms[room] = {
                    "name": name,
                    "roll": roll
                }
                print("Student registered successfully!")
            else:
                print("Room is already occupied.")
        else:
            print("Invalid room number.")

    def view_students(self):
        print("\n--- REGISTERED STUDENTS ---")
        found = False

        for room, student in self.rooms.items():
            if student is not None:
                print("Name:", student["name"])
                print("Roll Number:", student["roll"])
                print("Room Number:", room)
                print("----------------------")
                found = True

        if not found:
            print("No students registered.")

    def vacate_room(self):
        room = int(input("Enter room number: "))

        if room in self.rooms and self.rooms[room] is not None:
            print("Student", self.rooms[room]["name"], "has vacated the room.")
            self.rooms[room] = None
            print("Room vacated successfully!")
        else:
            print("Room is already vacant or invalid.")

    def hostel_fee(self):
        days = int(input("Enter number of days: "))
        fee = days * 300

        print("\n--- HOSTEL FEE DETAILS ---")
        print("Fee per day: Rs. 300")
        print("Number of days:", days)
        print("Total Hostel Fee: Rs.", fee)


hostel = Hostel()

while True:
    print("\n======= HOSTEL MANAGEMENT SYSTEM =======")
    print("1. Available Rooms")
    print("2. Register Student")
    print("3. Student Details")
    print("4. Vacate Room")
    print("5. Calculate Hostel Fee")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        hostel.view_rooms()

    elif choice == 2:
        hostel.register_student()

    elif choice == 3:
        hostel.view_students()

    elif choice == 4:
        hostel.vacate_room()

    elif choice == 5:
        hostel.hostel_fee()

    elif choice == 6:
        print("Thank you for using Hostel Management System!")
        break

    else:
        print("Invalid choice!")
