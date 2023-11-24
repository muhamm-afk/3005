import psycopg2
from psycopg2 import sql

parameters = {
    'host' : 'localhost',
    'database' : 'Student',
    'user' : 'postgres',
    'password' : 'Abdu11ah'  }

def connect():
    try:
        connection = psycopg2.connect(**parameters)
        return connection
    except psycopg2.Error as e:
        print(f"Error: Unable to connect to any such database\n{e}")
    return None


def create_student(connection, first_name, last_name, email, enrollment_date):
    try:
        with connection.cursor() as cursor:
            sql_query = sql.SQL("""
                                INSERT INTO students (first_name, last_name, email, enrollment_date)
                                VALUES (%s, %s, %s, %s)
                                RETURNING student_id;
                                """)
            cursor.execute(sql_query, (first_name, last_name, email, enrollment_date))
            student_id = cursor.fetchone()[0]
            connection.commit()
            return student_id
    except psycopg2.Error as e:
        print(f"Error: Unable to create new student attribute.\n{e}")
        connection.rollback()  # Rollback the transaction in case of an error
        return None

def read_students(connection):
    try:
        with connection.cursor() as cursor:
            sql_query = sql.SQL(" SELECT * FROM students")
            cursor.execute(sql_query)
            students = cursor.fetchall()
            return students
    except psycopg2.Error as e:
        print (f"Error: unable to read students.\n{e}")
        return None
    
def update_students(connection, student_id, new_email):
    try:
        with connection.cursor() as cursor:
            sql_query = sql.SQL("""
                                UPDATE students
                                SET email =%s
                                WHERE student_id = %s;
                                """)
            cursor.execute(sql_query, (new_email, student_id))
            connection.commit()
    except psycopg2.Error as e:
        print(f"Error: unable to update students.\n{e}")

def delete_student(connection, student_id):
    try:
        with connection.cursor() as cursor:
            sql_query = sql.SQL("""
                DELETE FROM students
                WHERE student_id = %s;
            """)
            cursor.execute(sql_query, (student_id,))
            connection.commit()
    except psycopg2.Error as e:
        print(f"Error: Unable to delete student.\n{e}")

def main():
    connection = connect()

    # Check if the connection was successful
    if connection is None:
        print("Exiting due to connection error.")
        return

    try:
        # Example: Create a new student
        student_id = create_student(connection, 'John', 'Doe', 'john.doe@email.com', '2023-01-01')

        # Check if student creation was successful
        if student_id is not None:
            print(f"Created student with ID: {student_id}")

            # Example: Read all students
            students = read_students(connection)

            # Check if reading students was successful
            if students is not None:
                print("All students:")
                for student in students:
                    print(student)
            else:
                print("Error reading students.")
        else:
            print("Error creating student.")

        # Example: Update a student's email
        update_students(connection, student_id, 'john.doe.updated@email.com')
        print("Updated student email.")

        # Example: Read all students after update
        students = read_students(connection)

        # Check if reading students after update was successful
        if students is not None:
            print("All students after update:")
            for student in students:
                print(student)
        else:
            print("Error reading students after update.")

        # Example: Delete a student
        delete_student(connection, student_id)
        print("Deleted student.")

        # Example: Read all students after delete
        students = read_students(connection)

        # Check if reading students after delete was successful
        if students is not None:
            print("All students after delete:")
            for student in students:
                print(student)
        else:
            print("Error reading students after delete.")

    finally:
        # Close the database connection in a 'finally' block to ensure it gets closed even if an exception occurs
        connection.close()

if __name__ == "__main__":
    main()
