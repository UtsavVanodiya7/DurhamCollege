from flask import Flask, request, render_template, redirect
from datetime import datetime
from models import db, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


@app.route('/')
def home():
    return "Welcome to simple student repository!"


@app.route('/student/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')

    if request.method == 'POST':
        student_id = request.form['student_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        y, m, d = request.form['dob'].split('-')
        dob = datetime(int(y), int(m), int(d))

        amount_due = request.form['amount_due']

        student = Student(student_id=student_id, first_name=first_name, last_name=last_name,
                          dob=dob, amount_due=amount_due)

        db.session.add(student)
        db.session.commit()

        return redirect('/student/all')


@app.route('/student/all')
def get_all_students():
    students = Student.query.all()
    return render_template('view_all.html', students=students)


@app.route('/student/<int:std_id>')
def get_student_by_id(std_id):
    student = Student.query.filter_by(student_id=std_id).first()

    if student:
        return render_template('view.html', student=student)

    return f"Student with id = {std_id} doesn't exist."


@app.route('/student/update/<int:std_id>', methods=['GET', 'POST'])
def update(std_id):
    if request.method == 'GET':
        student = Student.query.filter_by(student_id=std_id).first()

        if student:
            return render_template('update.html', student=student)

        return f"Student with id = {std_id} doesn't exist."

    if request.method == 'POST':
        student = Student.query.filter_by(student_id=std_id).first()

        if student:
            student.first_name = request.form['first_name']
            student.last_name = request.form['last_name']

            y, m, d = request.form['dob'].split('-')
            student.dob = datetime(int(y), int(m), int(d))

            student.amount_due = request.form['amount_due']

            db.session.commit()

    return redirect('/student/all')


@app.route('/student/delete/<int:std_id>')
def delete(std_id):
    student = Student.query.filter_by(student_id=std_id).first()

    if student:
        db.session.delete(student)
        db.session.commit()
        return redirect('/student/all')
    else:
        return f"Student with id = {std_id} doesn't exist."


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
