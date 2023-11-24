To run the python script the psycopg2 module must be downloaded first.

Within my a2.py script, you may have to change the following line 7 and 8 as they are referring to my sql user account so beware of that. yo will mostlikely have a different username and password. i have omiitted the password please fill it in with your own password

before this is done please verify that you have python downloaded using the following statements, if you do not have Python downloaded, you can download it using the link here --->https://www.python.org/downloads/

python --version

to download thIs module, first go to you're command shell and type the following if you are on windows:

pip install psycopg2-binary

once this is installed please open up the a2.py script and on command line or shell, get to the directory of a2.py

once you are at the directory, run the following command:

python3.10 a2.py

explanations of functions:

Connect:

Uses the psycopg2 library to connect to the database using the provided connection parameter then returns the database connection; otherwise, prints an error message and returns None.

create_student:

Takes a database connection and student details (first name, last name, email, enrollment date) as parameters then proceeds to use a sql inser to add a new student to the students table
Retrieves the generated student_id using RETURNING.
Commits the transaction if successful; otherwise, rolls back and prints an error message

read_students:

Takes a database connection as a parameter and uses a SQL SELECT query to fetch all student records from the 'students' table.
If an error occurs during the operation, prints an error message and returns None

update_students:

akes a database connection, student_id, and the new email as parameters and Uses a SQL UPDATE query to modify the email of the specified studen
Commits the transaction if its uccessful otherwise prints an error message

delete_student:

Takes a database connection and student_id as parameters and Uses a SQL DELETE query to remove the specified student record
Commits the transaction if successful otherwise, prints an error message

main:

first Calls the connect function to establish a database connection then proceeds to creates a new student, reads all students, updates the email of the created student, reads all students again, deletes the created student, and reads all students once more
finally closes the database connection in a finally block to ensure closure even in case of exceptions



https://www.loom.com/share/608beb3d475944928be79a7765ddf0a6?sid=ad194223-ce20-4330-a367-c6ad7546be5a
