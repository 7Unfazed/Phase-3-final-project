from models.students import Student
from models.courses import Course
from models.enrollment import Enrollment

def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enroll Student")
        print("4. List Students")
        print("5. List Courses")
        print("6. List Enrollments")
        print("7. Delete Student")
        print("8. Delete Course")
        print("9. Find Student by ID")
        print("10. Find Course by ID")
        print("11. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            Student.create(name, age)
            print("Student added successfully.")
        elif choice == '2':
            title = input("Enter course title: ")
            description = input("Enter course description: ")
            Course.create(title, description)
            print("Course added successfully.")
        elif choice == '3':
            student_id = int(input("Enter student ID: "))
            course_id = int(input("Enter course ID: "))
            Enrollment.create(student_id, course_id)
            print("Student enrolled successfully.")
        elif choice == '4':
            students = Student.get_all()
            print("\nList of Students:")
            for student in students:
                print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}")
        elif choice == '5':
            courses = Course.get_all()
            print("\nList of Courses:")
            for course in courses:
                print(f"ID: {course[0]}, Title: {course[1]}, Description: {course[2]}")
        elif choice == '6':
            enrollments = Enrollment.get_all()
            print("\nList of Enrollments:")
            for enrollment in enrollments:
                print(f"Student ID: {enrollment[0]}, Student Name: {enrollment[1]}, Course ID: {enrollment[2]}, Course Title: {enrollment[3]}")
        elif choice == '7':
            student_id = int(input("Enter student ID to delete: "))
            Student.delete(student_id)
            print("Student deleted successfully.")
        elif choice == '8':
            course_id = int(input("Enter course ID to delete: "))
            Course.delete(course_id)
            print("Course deleted successfully.")
        elif choice == '9':
            student_id = int(input("Enter student ID to find: "))
            student = Student.find_by_id(student_id)
            if student:
                print(f"Student found: ID: {student[0]}, Name: {student[1]}, Age: {student[2]}")
            else:
                print("Student not found.")
        elif choice == '10':
            course_id = int(input("Enter course ID to find: "))
            course = Course.find_by_id(course_id)
            if course:
                print(f"Course found: ID: {course[0]}, Title: {course[1]}, Description: {course[2]}")
            else:
                print("Course not found.")
        elif choice == '11':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
