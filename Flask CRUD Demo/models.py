from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    __tablename__ = "student"

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(db.Integer(), unique=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    dob = db.Column(db.Date())
    amount_due = db.Column(db.Float())

    def __init__(self, student_id, first_name, last_name, dob, amount_due):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.amount_due = amount_due

    def __repr__(self):
        return f"Student Id: {self.student_id}" \
               f"\nFirst Name: {self.first_name}" \
               f"\nLast Name: {self.last_name}" \
               f"\nDate of Birth: {self.dob}" \
               f"\nAmount Due: {self.amount_due}"
