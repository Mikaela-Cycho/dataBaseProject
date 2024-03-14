import psycopg2
from psycopg2 import sql

# Database connection parameters
conn_params = {
    'dbname': 'school',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost'
}

# cursor = connection.cursor()

# Function to connect to the database
def connect_db():
    conn = psycopg2.connect(**conn_params)
    return conn

# CRUD operations
def getAllStudents():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    records = cur.fetchall()
    for rec in records:
        print(rec)
    cur.close()
    conn.close()

def addStudent(first_name, last_name, email, enrollment_date):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, email, enrollment_date))
    conn.commit()
    cur.close()
    conn.close()

def updateStudentEmail(student_id, new_email):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s",
                (new_email, student_id))
    conn.commit()
    cur.close()
    conn.close()

def deleteStudent(student_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    conn.commit()
    cur.close()
    conn.close()

# Example Usage
if __name__ == "__main__":
    getAllStudents()
    addStudent('Alice', 'Wonderland', 'alice@example.com', '2023-10-01')
    updateStudentEmail(1, 'new.john.doe@example.com')
    deleteStudent(2)

# test commit