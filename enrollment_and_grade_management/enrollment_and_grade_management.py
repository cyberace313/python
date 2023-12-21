class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = []
        self.grades = {}

    def enroll_course(self, course):
        if len(self.enrolled_courses) < Course.MAX_CAPACITY:
            self.enrolled_courses.append(course)
            Course.enroll_student(self, course)
        else:
            print("Enrollment failed. Course has reached maximum capacity.")

    def assign_grade(self, course, grade):
        if course in self.enrolled_courses:
            self.grades[course.course_id] = grade
        else:
            print("Grade assignment failed. Student is not enrolled in the course.")

    def get_grade(self, course):
        return self.grades.get(course.course_id, -1)

    def calculate_overall_grade(self):
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)


class Course:
    MAX_CAPACITY = 10  # Example maximum capacity

    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.enrolled_students = []

    @classmethod
    def enroll_student(cls, student, course):
        cls.enrolled_students.append(student)
        print(f"{student.name} has been enrolled in the course {course.course_id}.")


class CourseManagement:
    courses = []
    overall_grades = {}

    @classmethod
    def add_course(cls, course_id, course_name):
        course = Course(course_id, course_name)
        cls.courses.append(course)
        print(f"Course added: {course.course_id} - {course.course_name}")

    @classmethod
    def enroll_student(cls, student, course):
        student.enroll_course(course)

    @classmethod
    def assign_grade(cls, student, course, grade):
        student.assign_grade(course, grade)
        print(f"Grade assigned to {student.name} for course {course.course_id}: {grade}")

    @classmethod
    def calculate_overall_grade(cls, student):
        overall_grade = student.calculate_overall_grade()
        print(f"Overall grade for {student.name}: {overall_grade}")


class AdministratorInterface:
    @staticmethod
    def display_menu():
        print("\n           Administrator Menu          ")
        print("1. Add a new course")
        print("2. Enroll a student")
        print("3. Assign a grade")
        print("4. Calculate overall course grades for a student")
        print("5. Exit")

    @staticmethod
    def add_course():
        course_id = input("Enter the course code: ")
        course_name = input("Enter the course name: ")
        CourseManagement.add_course(course_id, course_name)

    @staticmethod
    def enroll_student():
        student_id = input("Enter the student ID: ")
        # Search for the student in the system (not implemented in this basic example)

        course_id = input("Enter the course code to enroll the student: ")
        # Search for the course in the system (not implemented in this basic example)

        student = Student(student_id, "Vladimir Putin")  # Assuming a new student is created for simplicity
        course = Course(course_id, "Math")  # Assuming a new course is created for simplicity
        CourseManagement.enroll_student(student, course)

    @staticmethod
    def assign_grade():
        student_id = input("Enter the student ID: ")
        # Search for the student in the system (not implemented in this basic example)

        course_id = input("Enter the course code to assign a grade: ")
        # Search for the course in the system (not implemented in this basic example)

        grade = int(input("Enter the grade to assign: "))
        student = Student(student_id, "Vladimir Putin")  # Assuming an existing student is used for simplicity
        course = Course(course_id, "Math")  # Assuming an existing course is used for simplicity
        CourseManagement.assign_grade(student, course, grade)

    @staticmethod
    def calculate_overall_grade():
        student_id = input("Enter the student ID: ")
        # Search for the student in the system (not implemented in this basic example)

        student = Student(student_id, "Vladimir Putin")  # Assuming an existing student is used for simplicity
        CourseManagement.calculate_overall_grade(student)


def main():
    choice = 0

    while choice != 5:
        AdministratorInterface.display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            AdministratorInterface.add_course()
        elif choice == 2:
            AdministratorInterface.enroll_student()
        elif choice == 3:
            AdministratorInterface.assign_grade()
        elif choice == 4:
            AdministratorInterface.calculate_overall_grade()
        elif choice == 5:
            print("Exiting the system.")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

