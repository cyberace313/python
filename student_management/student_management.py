class Student:
    def __init__(self, name, student_id, age, grade):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


class StudentManagement:
    student_list = []
    total_students = 0

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)
        cls.total_students += 1

    @classmethod
    def find_student_by_id(cls, student_id):
        for student in cls.student_list:
            if student.student_id == student_id:
                return student
        return None  # Student not found

    @classmethod
    def update_student(cls, student, age, grade):
        student.age = age
        student.grade = grade

    @classmethod
    def display_all_students(cls):
        for student in cls.student_list:
            print(student)

    @classmethod
    def get_total_students(cls):
        return cls.total_students


def add_new_student():
    name = input("Enter student name: ")
    student_id = int(input("Enter student ID: "))
    age = int(input("Enter student age: "))
    grade = float(input("Enter student grade: "))

    new_student = Student(name, student_id, age, grade)
    StudentManagement.add_student(new_student)

    print("New student added successfully!")


def update_student_info():
    student_id = int(input("Enter student ID to update information: "))
    student_to_update = StudentManagement.find_student_by_id(student_id)

    if student_to_update:
        new_age = int(input("Enter new age: "))
        new_grade = float(input("Enter new grade: "))

        StudentManagement.update_student(student_to_update, new_age, new_grade)
        print("Student information updated successfully!")
    else:
        print(f"Student not found with ID: {student_id}")


def view_student_details():
    print("All Students:")
    StudentManagement.display_all_students()
    print(f"Total Students: {StudentManagement.get_total_students()}")


def main():
    while True:
        print("\nStudent Record Management System")
        print("1. Add a new student")
        print("2. Update student information")
        print("3. View student details")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            add_new_student()
        elif choice == '2':
            update_student_info()
        elif choice == '3':
            view_student_details()
        elif choice == '4':
            print("Exiting Student Record Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
