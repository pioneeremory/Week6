# We import the `Flask` and `jsonify` classes from the Flask library.
import struct
from flask import Flask, jsonify

# We create a Flask application by initializing the `app` object.
app = Flask(__name__)

students = [
     {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
     {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
     {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
     {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
     {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
     {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
     {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
     {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
     {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
     {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
 ]

# We define a route `/students` that responds to GET requests.
@app.route('/students', methods=['GET'])
def home():
    return "<h1>Welcome to the Student API</h1><p>Go to <a href='/students'>/students</a> for the data.</p>", 200

def get_students():
    return jsonify(students)
# /old_students/: Returns an array of student objects where the students are older than 20 years old
@app.route('/students/old_students', methods=['GET'])
def get_old_students():
    old_students = []
    for student in students:
        if student ['age'] > 20:
            old_students.append(student)
    if old_students:
        return jsonify(old_students)
    else: 
        return "No students older than 20 years old", 404
    
# /young_students/: Returns an array of student objects where the students are younger than 21 years old.
@app.route('/students/young_students', methods=['GET'])
def young_students():
    young_students = []
    for student in students:
        if student ['age'] < 21:
            young_students.append(student)
    if young_students:
        return jsonify(young_students)
    else: 
        return "No students younger than 21 years old", 404

# /advance_students/: Returns an array of student objects where the students are younger than 21 and have a letter grade of "A."
@app.route('/students/advance_students', methods=['GET'])
def advance_students():
    advance_students = []
    for student in students:
        if student ['age'] < 21 and student['grade'] == 'A':
            advance_students.append(student)
    if advance_students:
        return jsonify(advance_students)
    else: 
        return "No young smart students", 404
# /student_names/: Returns an array of student objects holding only the keys of 'first_name' and 'last_name' along with their corresponding values.
@app.route('/students/student_names', methods=['GET'])
def student_names():
    student_names = []
    for student in students:
        student_names.append(student['first_name'])
        student_names.append(student['last_name'])
    if student_names:
        return jsonify(student_names)
    else: 
        return "No young smart students", 404
# /student_ages/: Returns an array of student objects holding the keys 'student_name' with the value of first and last name, and 'age' with the value of that student's age.
@app.route('/students/student_ages', methods=['GET'])
def student_ages():
    student_ages = []
    for student in students:
        student_ages.append(student['first_name'])
        student_ages.append(student['last_name'])
    if student_ages:
        return jsonify(student_ages)
    else: 
        return "There are no students", 404

# /students/: Returns an array of all student objects available.


if __name__ == '__main__':
    app.run(debug=True) 