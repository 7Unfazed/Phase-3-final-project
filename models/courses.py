import sqlite3
from Database.connection import get_connection

class Course:
    @staticmethod
    def create(title, description):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO courses (title, description) VALUES (?, ?)', (title, description))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(course_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM courses WHERE id = ?', (course_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM courses')
            courses = cursor.fetchall()
            conn.close()
            return courses
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []

    @staticmethod
    def find_by_id(course_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM courses WHERE id = ?', (course_id,))
            course = cursor.fetchone()
            conn.close()
            return course
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return None
