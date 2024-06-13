import sqlite3
from Database.connection import get_connection

class Student:
    @staticmethod
    def create(name, age):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO students (name, age) VALUES (?, ?)', (name, age))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(student_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM students')
            students = cursor.fetchall()
            conn.close()
            return students
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []

    @staticmethod
    def find_by_id(student_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
            student = cursor.fetchone()
            conn.close()
            return student
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return None
