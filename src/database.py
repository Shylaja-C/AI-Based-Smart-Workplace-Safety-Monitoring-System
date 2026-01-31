import sqlite3
import os

class EmployeeDB:
    def __init__(self, db_path='data/employees.db'):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            employee_id TEXT UNIQUE,
            unique_number TEXT UNIQUE,
            name TEXT
        )''')
        self.conn.commit()

    def add_employee(self, employee_id, unique_number, name):
        try:
            self.conn.execute('INSERT INTO employees (employee_id, unique_number, name) VALUES (?, ?, ?)', (employee_id, unique_number, name))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def get_employee(self, unique_number):
        cursor = self.conn.execute('SELECT * FROM employees WHERE unique_number = ?', (unique_number,))
        return cursor.fetchone()

    def is_authorized(self, unique_number):
        return self.get_employee(unique_number) is not None

    def close(self):
        self.conn.close()