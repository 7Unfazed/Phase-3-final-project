import sqlite3
from Database.connection import get_connection

class Enrollment:
    @staticmethod
    def create(student_id, course_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)', (student_id, course_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(student_id, course_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM enrollments WHERE student_id = ? AND course_id = ?', (student_id, course_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute('''
                SELECT students.id, students.name, courses.id, courses.title
                FROM enrollments
                JOIN students ON enrollments.student_id = students.id
                JOIN courses ON enrollments.course_id = courses.id
            ''')
            enrollments = cursor.fetchall()
            conn.close()
            return enrollments
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []

    @staticmethod
    def find_by_id(student_id, course_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute('''
                SELECT students.id, students.name, courses.id, courses.title
                FROM enrollments
                JOIN students ON enrollments.student_id = students.id
                JOIN courses ON enrollments.course_id = courses.id
                WHERE enrollments.student_id = ? AND enrollments.course_id = ?
            ''', (student_id, course_id))
            enrollment = cursor.fetchone()
            conn.close()
            return enrollment
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return None
