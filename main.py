from students.student_manager import StudentManager
from departments.department_manager import DepartmentManager


def main_menu():
    print("\n==== Student Record Management System ====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Add Department")
    print("6. View Departments")
    print("7. Exit")
    print("==========================================")


def show_student(s, idx=None):
    if idx is not None:
        print(f"{idx}. Name : {s.name}")
    else:
        print(f"Name : {s.name}")

    print(f"   Roll : {s.roll}")
    print(f"   Email : {s.email}")
    print(f"   Department : {s.department}")
    print("----------------------")


def main():
    student_manager = StudentManager()
    dept_manager = DepartmentManager()

    print("Welcome to the Student Record Management System!")
    print("Loading records...", end=" ")

    if student_manager.students:
        print("Done!")
    else:
        print("No data found.")


    while True:
        main_menu()
        choice = input("Enter choice: ").strip()

        # 1) Add Student
        if choice == "1":
            print("\n--- Add Student ---")

            name = input("Enter Student Name: ").strip()
            if not name:
                print("Error: Empty input is not allowed.")
                input("\nPress Enter to continue...")
                continue

            if not any(ch.isalpha() for ch in name):
                print("Error: Student name must contain letters.")
                input("\nPress Enter to continue...")
                continue


            roll_input = input("Enter Roll Number: ").strip()
            if not roll_input:
                print("Error: Empty input is not allowed.")
                input("\nPress Enter to continue...")
                continue
            if not roll_input.isdigit():
                print("Error: Roll number must be an integer.")
                input("\nPress Enter to continue...")
                continue
            roll = int(roll_input)

            email = input("Enter Email: ").strip().lower()
            if not email:
                print("Error: Empty input is not allowed.")
                input("\nPress Enter to continue...")
                continue
            if "@" not in email or "." not in email:
                print("Error: Please enter a valid email address.")
                input("\nPress Enter to continue...")
                continue

            department = input("Enter Department: ").strip()
            if not department:
                print("Error: Empty input is not allowed.")
                input("\nPress Enter to continue...")
                continue

            # Department validation (optional)
            # If at least one department exists in departments.json, then validate the input
            if not dept_manager.exists(department):
                print("Error: Department not found. Please add the department first.")
                input("\nPress Enter to continue...")
                continue


            # Add using manager (returns None if roll number already exists)
            st = student_manager.add_student(roll, name, department, email)
            if st is None:
                print("Error: Roll number already exists for another student.")
            else:
                print("Student record added successfully!")

        # 2) View Students
        elif choice == "2":
            print("\n====== All Students ======")
            if not student_manager.students:
                print("No students found.")
            else:
                for i, s in enumerate(student_manager.students, start=1):
                    show_student(s, idx=i)
            print("==========================")

        # 3) Search Student
        elif choice == "3":
            print("\n--- Search Student ---")
            key = input("Enter search term (name/email/roll): ").strip().lower()
            if not key:
                print("Error: Empty input is not allowed.")
                input("\nPress Enter to continue...")
                continue

            results = student_manager.search_students(key)

            if results:
                print("\n-- Search Results --")
                for s in results:
                    show_student(s)
            else:
                print("No matching student found.")

        # 4) Remove Student
        elif choice == "4":
            print("\n--- Remove Student ---")
            roll_input = input("Enter the roll number of the student to delete: ").strip()
            if not roll_input:
                print("Error: Empty input is not allowed.")
                input("\nPress Enter to continue...")
                continue
            if not roll_input.isdigit():
                print("Error: Roll number must be an integer.")
                input("\nPress Enter to continue...")
                continue
            roll = int(roll_input)

            confirm = input(f"Are you sure you want to delete roll {roll}? (y/n): ").strip().lower()
            if confirm != "y":
                print("Delete cancelled.")
                input("\nPress Enter to continue...")
                continue

            ok = student_manager.remove_student(roll)
            if ok:
                print("Student record deleted successfully!")
            else:
                print("Error: Student not found with that roll number.")

        # 5) Add Department
        elif choice == "5":
            print("\n--- Add Department ---")
            dept_id = input("Enter Department ID: ").strip()
            if not dept_id:
                print("Error: Empty input is not allowed.")
                input("\nPress Enter to continue...")
                continue

            dept_name = input("Enter Department Name: ").strip()
            if not dept_name:
                print("Error: Empty input is not allowed.")
                input("\nPress Enter to continue...")
                continue

            dept_manager.add_department(dept_id, dept_name)

        # 6) View Departments
        elif choice == "6":
            dept_manager.list_departments()

        # 7) Exit
        elif choice == "7":
            print("Thank you for using the Student Record Management System. Goodbye!")
            break

        else:
            print("Invalid choice!")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
