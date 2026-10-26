
# STUDENT RECORD MANAGEMENT SYSTEM
# DSA Mini-Project
# Language: Python

students = []


# 1. Add Student
def add_student():
    print("\n--- ADD STUDENT ---")

    student_id = input("Enter Student ID: ").strip()

    if not student_id:
        print("Error: Student ID cannot be empty.")
        return

    if any(s["id"] == student_id for s in students):
        print("Error: Student ID already exists.")
        return

    name = input("Enter Student Name: ").strip()
    course = input("Enter Course: ").strip()

    try:
        marks = float(input("Enter Marks (0-100): "))

        if not 0 <= marks <= 100:
            print("Error: Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Error: Please enter valid numeric marks.")
        return

    if not name or not course:
        print("Error: Name and course cannot be empty.")
        return

    student = {
        "id": student_id,
        "name": name,
        "course": course,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")


# 2. Display Students
def display_students():
    print("\n--- ALL STUDENT RECORDS ---")

    if not students:
        print("No student records found.")
        return

    print("-" * 75)
    print(
        f"{'ID':<12}{'NAME':<22}"
        f"{'COURSE':<20}{'MARKS':<10}{'GRADE':<10}"
    )
    print("-" * 75)

    for student in students:
        print(
            f"{student['id']:<12}"
            f"{student['name']:<22}"
            f"{student['course']:<20}"
            f"{student['marks']:<10.2f}"
            f"{calculate_grade(student['marks']):<10}"
        )

    print("-" * 75)


# 3. Calculate Grade
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


# 4. Linear Search
def linear_search(student_id):
    for student in students:
        if student["id"] == student_id:
            return student

    return None


# 5. Search Student
def search_student():
    print("\n--- SEARCH STUDENT ---")

    student_id = input("Enter Student ID to search: ").strip()

    student = linear_search(student_id)

    if student:
        print("\nStudent Found!")
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Course:", student["course"])
        print("Marks:", student["marks"])
        print("Grade:", calculate_grade(student["marks"]))
    else:
        print("Student not found.")


# 6. Update Student
def update_student():
    print("\n--- UPDATE STUDENT ---")

    student_id = input("Enter Student ID to update: ").strip()
    student = linear_search(student_id)

    if not student:
        print("Student not found.")
        return

    print("Press Enter to keep the existing value.")

    name = input(f"Name [{student['name']}]: ").strip()
    course = input(f"Course [{student['course']}]: ").strip()
    marks_input = input(f"Marks [{student['marks']}]: ").strip()

    if name:
        student["name"] = name

    if course:
        student["course"] = course

    if marks_input:
        try:
            marks = float(marks_input)

            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100.")
                return

            student["marks"] = marks

        except ValueError:
            print("Invalid marks. Marks were not updated.")
            return

    print("Student record updated successfully!")


# 7. Delete Student
def delete_student():
    print("\n--- DELETE STUDENT ---")

    student_id = input("Enter Student ID to delete: ").strip()
    student = linear_search(student_id)

    if not student:
        print("Student not found.")
        return

    confirmation = input(
        f"Delete record for {student['name']}? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
        students.remove(student)
        print("Student record deleted successfully!")
    else:
        print("Deletion cancelled.")


# 8. Bubble Sort by Marks
def bubble_sort_by_marks():
    print("\n--- SORT STUDENTS BY MARKS ---")

    if not students:
        print("No student records to sort.")
        return

    n = len(students)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if students[j]["marks"] > students[j + 1]["marks"]:
                students[j], students[j + 1] = (
                    students[j + 1],
                    students[j]
                )
                swapped = True

        if not swapped:
            break

    print("Students sorted by marks in ascending order.")
    display_students()


# 9. Binary Search by Student ID
def binary_search_by_id(student_id):
    # Binary Search requires records sorted by ID.
    sorted_students = sorted(students, key=lambda s: s["id"])

    low = 0
    high = len(sorted_students) - 1

    while low <= high:
        mid = (low + high) // 2
        current_id = sorted_students[mid]["id"]

        if current_id == student_id:
            return sorted_students[mid]

        elif current_id < student_id:
            low = mid + 1

        else:
            high = mid - 1

    return None


# 10. Binary Search Menu
def binary_search_student():
    print("\n--- BINARY SEARCH BY STUDENT ID ---")

    if not students:
        print("No student records available.")
        return

    student_id = input("Enter Student ID to search: ").strip()

    student = binary_search_by_id(student_id)

    if student:
        print("\nStudent Found!")
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Course:", student["course"])
        print("Marks:", student["marks"])
        print("Grade:", calculate_grade(student["marks"]))
    else:
        print("Student not found.")


# 11. Main Menu
def main():
    while True:
        print("\n" + "=" * 45)
        print(" STUDENT RECORD MANAGEMENT SYSTEM")
        print("=" * 45)
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student (Linear Search)")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Sort Students by Marks (Bubble Sort)")
        print("7. Search Student (Binary Search)")
        print("8. Exit")
        print("=" * 45)

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            bubble_sort_by_marks()
        elif choice == "7":
            binary_search_student()
        elif choice == "8":
            print("Thank you for using the Student Record Management System!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()

