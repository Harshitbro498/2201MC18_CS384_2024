def add_student(students, name, grades):
    name = name.lower()
    students[name] = grades

def update_grades(students, name, new_grades):
    name = name.lower()
    if name in students:
        students[name] = new_grades
    else:
        print(f"Student '{name}' does not exist.")

def calculate_average(students):
    averages = {}
    for name, grades in students.items():
        averages[name] = sum(grades) / len(grades) if grades else 0
    return averages

def print_students_with_averages(students):
    averages = calculate_average(students)
    for name, avg in averages.items():
        print(f"{name.capitalize()} - Average: {avg:.2f}")

def sort_students_by_average(students):
    averages = calculate_average(students)
    sorted_students = []
    for student, avg in averages.items():
        inserted = False
        for i in range(len(sorted_students)):
            if avg > averages[sorted_students[i]]:
                sorted_students.insert(i, student)
                inserted = True
                break
        if not inserted:
            sorted_students.append(student)
    return sorted_students

def main():
    students = {}

    while True:
        print("\nOptions:")
        print("1. Add a new student with grades")
        print("2. Update grades of an existing student")
        print("3. Calculate and print average grades of all students")
        print("4. Print students sorted by average grades")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            grades = list(map(int, input("Enter grades separated by spaces: ").split()))
            add_student(students, name, grades)
        elif choice == '2':
            name = input("Enter student name: ")
            grades = list(map(int, input("Enter new grades separated by spaces: ").split()))
            update_grades(students, name, grades)
        elif choice == '3':
            print_students_with_averages(students)
        elif choice == '4':
            sorted_students = sort_students_by_average(students)
            print("\nStudents sorted by average grades:")
            for student in sorted_students:
                avg = sum(students[student]) / len(students[student])
                print(f"{student.capitalize()} - Average: {avg:.2f}")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
