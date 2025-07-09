students = []
def add_student():
    student_id = input("Enter student ID: ")
    if any(student["id"] == student_id for student in students):
        print("A student with this ID already exists.\n")
        return

    name = input("Enter student name: ")
    department=input("Enter student department: ")
    section=input("Enter student section: ")
    year=input("Enter year of studying: ")
    stu_join=input("Enter student joining year: ")
    student = {"id": student_id, "name": name,"department":department,"section":section,"year":year,"year of joining":stu_join}
    students.append(student)
    print(f"Student {name} with ID {student_id} added successfully.\n")

def view_student():
    student_id = input("Enter the student ID to view details: ")
    for student in students:
        if student["id"] == student_id:
            print("\nStudent Details:")
            print(f"ID              : {student['id']}")
            print(f"Name            : {student['name']}")
            print(f"Department      : {student['department']}")
            print(f"Section         : {student['section']}")
            print(f"Year            : {student['year']}")
            print(f"Year of Joining : {student['year of joining']}")
            return
    print("Student not found.\n")

def remove_student():
    student_id = input("Enter the student ID to remove: ")
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print(f"Student with ID {student_id} has been removed successfully.\n")
            return
    print("Student not found.\n")
def alldata():
    for student in students:
        print("\nStudent Details:")
        print(f"ID              : {student['id']}")
        print(f"Name            : {student['name']}")
        print(f"Department      : {student['department']}")
        print(f"Section         : {student['section']}")
        print(f"Year            : {student['year']}")
        print(f"Year of Joining : {student['year of joining']}")
        
def display_menu():
    """Display the main menu."""
    print("Student Database Menu:")
    print("1. Add Student")
    print("2. View Student")
    print("3. Remove Student")
    print("4. To View All Students Data")
    print("5. To Update the Students Data into Text file")
    print("6. To View Students Data in the Text File")
    print("7. Exit")
def update():
    f=open("DATA.txt","a+")
    b=str(students)
    f.write(b)
    print(f.read())
    f.close()
    print("DATA UPDATED TO TEXT DOCUMENT SUCCESSFULLY")
def viewdata():
    f=open("DATA.txt","r")
    print(f.read())
    f.close()

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            remove_student()
        elif choice == "4":
            alldata()
        elif choice == "5":
            update()
        elif choice == "6":
            viewdata()
        elif choice == "7":
            print("Exiting the Student Database. Goodbye!")
            break
        else:
            print("Invalid choice! Please select an option between 1 and 7.\n")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
