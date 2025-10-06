# ------------------------------
# 📘 Student Database System
# ------------------------------

info = {}
subjects = ["Maths", "English", "Physics", "Chemistry", "Geography"]

def add_student():
    """Add a new student and their subject scores."""
    try:
        name = input("Enter the student name: ").strip()
        student_id = int(input("Enter student ID: "))
        students = {"name": name, "id": student_id, "grades": {}}
        for subject in subjects:
            score = int(input(f"Enter the {subject} score: "))
            students["grades"][subject] = score
        info[name.lower()] = students
        print(f"✅ Student '{name}' added successfully.")
    except ValueError:
        print("❌ Invalid input. Please enter valid numbers.")

def search_student():
    """Search for a student by name."""
    search = input("Enter the student name to search: ").lower()
    if search in info:
        student = info[search]
        print("\n--- Student Details ---")
        print(f"Name: {student['name']}")
        print(f"ID: {student['id']}")
        print("Grades:")
        for subject, grade in student["grades"].items():
            print(f"  {subject}: {grade}")
    else:
        print("⚠️ Student not found in the database.")

def get_average(name):
    """Calculate average marks for a student."""
    try:
        grades = info[name.lower()]["grades"]
        avg = sum(grades.values()) / len(grades)
        return avg
    except KeyError:
        print("⚠️ Student not found.")
        return None

# ------------------------------
# 🎓 Main Menu
# ------------------------------
while True:
    print("\n__ Student Database __")
    print("1. Add new student")
    print("2. Search for a student")
    print("3. Get average for a student")
    print("4. Quit")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_student()
        elif choice == 2:
            search_student()
        elif choice == 3:
            name = input("Enter the student's name: ")
            avg = get_average(name)
            if avg is not None:
                print(f"Average marks for {name}: {avg:.2f}")
        elif choice == 4:
            print("👋 Exiting the system. Have a great day!")
            break
        else:
            print("❌ Invalid menu option.")
    except ValueError:
        print("❌ Please enter a number from the menu.")
