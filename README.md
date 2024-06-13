## Introduction 
  I'm required to write a program that creates an efficient system to manage student, course, and enrollment data. The Student Management System (SMS) aims to simplify these tasks by providing functionalities to add and list students and courses, enroll students in courses, and retrieve relevant information as well as deleting a student or a course

## Expectations
It should add a student, add a course and enroll a student to the database.It should also enable the user to delete a student and a course.To make retrival of data more effecient. The user will be able to find a student by the use of the student's Id. This should apply to the course as well
## How to Use
1. Pipenv install. Inorder to install the dependancy
2. Pipenv shell. To enter the environment
3. Use "python app.py" to open the menu
4. Then follow the instructions provided in the Terminal
5. You can exit by entering the number 11
## Implementation Details
The Student Management System is a Command Line Interface (CLI) application designed to manage students, courses, and enrollments. The system uses Object-Oriented Programming (OOP) principles and SQLAlchemy ORM to interact with an SQLite3 database. It supports adding students, courses, and enrollments, and retrieving information from the database.
## Relationships
1. One-to-Many Relationship (Students to Enrollments):
A student can enroll in many courses.
Each enrollment record refers to one student.

2. One-to-Many Relationship (Courses to Enrollments):
A course can have many students enrolled.
Each enrollment record refers to one course.

3. Many-to-Many Relationship (Students and Courses):
This is represented through the Enrolments table.
A student can enroll in multiple courses.
A course can have multiple students.

## Author
This  Student Management System program was created by Elvis Moses.

# Phase-3-final-project
