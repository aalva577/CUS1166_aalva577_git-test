from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    course_number = db.Column(db.String)
    course_title = db.Column(db.String)
    students = db.relationship('RegisteredStudent', secondary='link')

class RegisteredStudent(db.Model):
    __tablename__ = 'registeredstudent'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    grade = db.Column(db.Integer)
    courses = db.relationship('Course', secondary='link')

## Enroll students into db class
