from app import db


class User(db.Model):
  __tablename__ = 'users'
  student_id = db.Column(db.String,
                         primary_key=True,
                         nullable=False,
                         unique=True)
  password = db.Column(db.String(20), nullable=False)
  role = db.Column(db.String(20), nullable=False)


class StudentDetails(db.Model):

  def __init__(self, name, email, gender, dob, blood_group, mobile, address,
               student_id):
    self.name = name
    self.email = email
    self.gender = gender
    self.dob = dob
    self.blood_group = blood_group
    self.mobile = mobile
    self.address = address
    self.student_id = student_id

  __tablename__ = 'studentdetails'
  id = db.Column(db.Integer,
                 primary_key=True,
                 nullable=False,
                 unique=True,
                 autoincrement=True)
  name = db.Column(db.String(80), nullable=False)
  email = db.Column(db.String(80), nullable=False)
  gender = db.Column(db.String(10), nullable=False)
  dob = db.Column(db.String(10), nullable=False)
  blood_group = db.Column(db.String(5), nullable=False)
  mobile = db.Column(db.String(15), nullable=False)
  address = db.Column(db.String(255), nullable=False)
  student_id = db.Column(db.Integer,
                         db.ForeignKey('users.student_id'),
                         nullable=False)


class Courses(db.Model):
  __tablename__ = 'courses'
  id = db.Column(db.Integer,
                 primary_key=True,
                 nullable=False,
                 unique=True,
                 autoincrement=True)
  coursename = db.Column(db.String(80), nullable=False)
  course_instructor = db.Column(db.String(80), nullable=False)
  term = db.Column(db.String(20), nullable=False)
  course_id = db.Column(db.String(20), unique=True, nullable=False)


class StudentCourses(db.Model):
  __tablename__ = 'studentcourses'
  id = db.Column(db.Integer,
                 primary_key=True,
                 nullable=False,
                 unique=True,
                 autoincrement=True)
  student_id = db.Column(db.Integer,
                         db.ForeignKey('users.student_id'),
                         nullable=False)
  term = db.Column(db.String(20), nullable=False)
  course_id = db.Column(db.String(20),
                        db.ForeignKey('courses.course_id'),
                        nullable=False)
  coursename = db.Column(db.String(80),
                         db.ForeignKey('courses.coursename'),
                         nullable=False)
  course_instructor = db.Column(db.String(80),
                                db.ForeignKey('courses.course_instructor'),
                                nullable=False)
  feedback = db.Column(db.String(255), nullable=True)


class StudentMarks(db.Model):
  __tablename__ = 'studentmarks'
  id = db.Column(db.Integer, primary_key=True)
  student_id = db.Column(db.Integer,
                         db.ForeignKey('users.student_id'),
                         nullable=False)
  course_id = db.Column(db.String(20),
                        db.ForeignKey('courses.course_id'),
                        nullable=False)
  ass1 = db.Column(db.Integer, nullable=True)
  ass2 = db.Column(db.Integer, nullable=True)
  ass3 = db.Column(db.Integer, nullable=True)
  ass4 = db.Column(db.Integer, nullable=True)
  ass5 = db.Column(db.Integer, nullable=True)
  ass6 = db.Column(db.Integer, nullable=True)
  ass7 = db.Column(db.Integer, nullable=True)
  ass8 = db.Column(db.Integer, nullable=True)
  ass9 = db.Column(db.Integer, nullable=True)
  ass10 = db.Column(db.Integer, nullable=True)
  ass11 = db.Column(db.Integer, nullable=True)
  ass12 = db.Column(db.Integer, nullable=True)
  q1 = db.Column(db.Integer, nullable=True)
  q2 = db.Column(db.Integer, nullable=True)
  endterm = db.Column(db.Integer, nullable=True)


db.create_all()
db.session.commit()
