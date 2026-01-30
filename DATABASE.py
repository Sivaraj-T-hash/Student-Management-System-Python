import os

students = []
DATA_FILE = "DATA.txt"

def load_data():
    """Restores student records from the text file when the program starts."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                lines = f.readlines()
                # Skip the two header lines
                for line in lines[2:]:
                    parts = [p.strip() for p in line.split("|")]
                    if len(parts) == 6:
                        students.append({
                            "id": parts[0], "name": parts[1], "dept": parts[2],
                            "sec": parts[3], "year": parts[4], "joined": parts[5]
                        })
        except Exception as e:
            print(f"Loading error: {e}")

def add_student():
    sid = input("Enter ID: ")
    if any(s["id"] == sid for s in students):
        print("Error: ID already exists.")
        return
    
    student = {
        "id": sid,
        "name": input("Name: "),
        "dept": input("Department: "),
        "sec": input("Section: "),
        "year": input("Current Year: "),
        "joined": input("Joining Year: ")
    }
    students.append(student)
    print("Success: Student added.")

def update_file():
    """Saves records in a clean, readable table format."""
    with open(DATA_FILE, "w") as f:
        f.write(f"{'ID':<10} | {'Name':<20} | {'Dept':<15} | {'Sec':<5} | {'Year':<5} | {'Joined':<10}\n")
        f.write("-" * 80 + "\n")
        for s in students:
            f.write(f"{s['id']:<10} | {s['name']:<20} | {s['dept']:<15} | {s['sec']:<5} | {s['year']:<5} | {s['joined']:<10}\n")
    print("Database saved to DATA.txt.")

def main():
    load_data()
    while True:
        print("\n1. Add | 2. View All | 3. Save | 4. Exit")
        choice = input("Select: ")
        if choice == "1": add_student()
        elif choice == "2":
            for s in students: print(f"ID: {s['id']} | Name: {s['name']}")
        elif choice == "3": update_file()
        elif choice == "4": break

if __name__ == "__main__":
    main()
