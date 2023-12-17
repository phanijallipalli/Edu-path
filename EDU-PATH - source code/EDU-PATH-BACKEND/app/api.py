from flask_restful import Resource
from flask_restful import reqparse
from .database import db
from app import db
from flask import jsonify
from .model import User, StudentDetails, StudentCourses, Courses
from textblob import TextBlob

#----------------loginAPI------------
create_signup_parser = reqparse.RequestParser()
create_signup_parser.add_argument("userid")
create_signup_parser.add_argument("password")
create_signup_parser.add_argument("role")


class SignupAPI(Resource):

  def post(self):
    args = create_signup_parser.parse_args()
    sid = args.get("userid", None)
    password = args.get("password", None)
    role = args.get("role", None)
    print(sid, password, role)
    if (type(sid) is str) and (sid is not None) and (
        type(password) is str) and (password is not None) and (password != ""):
      user = User.query.filter_by(student_id=sid).first()
      if user:
        return jsonify({
            "statuscode": 409,
            "message": "username already exists"
        })

      else:
        new_user = User()
        new_user.student_id = sid
        new_user.password = password
        new_user.role = role
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"statuscode": 201, "message": "user created success"})
    else:
      return jsonify({"statuscode": 500, "message": "internal server error"})

  def put(self):
    args = create_signup_parser.parse_args()
    sid = args.get("userid", None)
    password = args.get("password", None)
    role = args.get("role", None)
    if (type(sid) is str) and (sid is not None) and (
        type(password) is str) and (password is not None) and (password != ""):
      user = User.query.filter_by(student_id=sid.first())
      if user:
        user.student_id = sid
        user.password = password
        user.role = role
        db.session.commit()
        return jsonify({"statuscode": 200, "message": "user updated success"})
      else:
        return jsonify({"statuscode": 409, "message": "user not exists"})


#updating sign up details: PENDING

#login----------------------------------
login_parser = reqparse.RequestParser()
login_parser.add_argument("userid")
login_parser.add_argument("password")
login_parser.add_argument("role")


class LoginAPI(Resource):

  def post(self):
    args = login_parser.parse_args()
    sid = args.get("userid", None)
    password = args.get("password", None)
    role = args.get("role", None)
    print(sid, password, role)
    if (type(sid) is str) and (sid is not None) and (
        type(password) is str) and (password is not None) and (password != ""):
      user = User.query.filter_by(student_id=sid).first()
      if user:
        if user.password == password:
          if user.role == role:
            return jsonify({
                "statuscode": 200,
                "message": "logged in succesfully"
            })
          else:
            return jsonify({
                "statuscode": 200,
                "message": "role doesn't match"
            })
        else:
          return jsonify({
              "statuscode": 200,
              "message": "passwords doesn't match"
          })

      else:
        return jsonify({
            "statuscode": 200,
            "message": "user not found sign up"
        })
    else:
      return jsonify({"statuscode": 500, "message": "internal server error"})


#/student_dasboard/student_details/{studentId} student details

studet = reqparse.RequestParser()
studet.add_argument("name")
studet.add_argument("email")
studet.add_argument("mobile")
studet.add_argument("address")
studet.add_argument("gender")
studet.add_argument("dob")
studet.add_argument("blood_group")


class StudentDetailsAPI(Resource):

  def get(self, studentId):
    user = StudentDetails.query.filter_by(student_id=studentId).first()
    if user:
      return jsonify({
          "statuscode": 200,
          "message": "student details",
          "studentId": user.student_id,
          "name": user.name,
          "email": user.email,
          "gender": user.gender,
          "dob": user.dob,
          "blood_group": user.blood_group,
          "mobile": user.mobile,
          "address": user.address,
      })
    else:
      return jsonify({
          "statuscode": 500,
          "message": "student not exist access not possible"
      })

  def post(self, studentId):
    args = studet.parse_args()
    name = args.get("name", None)
    email = args.get("email", None)
    mobile = args.get("mobile", None)
    address = args.get("address", None)
    dob = args.get("dob", None)
    gender = args.get("gender", None)
    blood_group = args.get("blood_group", None)

    user = StudentDetails.query.filter_by(student_id=studentId).first()
    if user:
      return jsonify({
          "statuscode": 409,
          "message": "Student details already exists"
      })
    else:
      new_user = StudentDetails(name=name,
                                email=email,
                                mobile=mobile,
                                address=address,
                                dob=dob,
                                gender=gender,
                                blood_group=blood_group,
                                student_id=studentId)

      db.session.add(new_user)
      db.session.commit()
      return jsonify({
          "statuscode": 201,
          "message": "Student created successfully"
      })

  def put(self, studentId):
    args = studet.parse_args()
    name = args.get("name", None)
    email = args.get("email", None)
    mobile = args.get("mobile", None)
    address = args.get("address", None)
    dob = args.get("dob", None)
    gender = args.get("gender", None)
    blood_group = args.get("blood_group", None)
    user = StudentDetails.query.filter_by(student_id=studentId).first()
    if user:
      user.name = name
      user.email = email
      user.mobile = mobile
      user.address = address
      user.dob = dob
      user.gender = gender
      user.blood_group = blood_group
      db.session.commit()
      return jsonify({
          "statuscode": 201,
          "message": "Student details updated successfully"
      })
    else:
      return jsonify({"statuscode": 204, "message": "student data not exists"})


#  /student_dasboard/student_courses/{studentId}: student courses
stucourse = reqparse.RequestParser()
stucourse.add_argument("course_id")
stucourse.add_argument("course_name")
stucourse.add_argument("course_instructor")
stucourse.add_argument("term")


class StudentCoursesAPI(Resource):

  def get(self, studentId):
    user = StudentCourses.query.filter_by(student_id=studentId).all()
    if user:
      value = []
      for course in user:
        course_data = {
            "course_id": course.course_id,
            "course_name": course.coursename,
            "course_instructor": course.course_instructor,
            "term": course.term
        }
        value.append(course_data)

      return jsonify({
          "statuscode": 200,
          "message": "student courses",
          "courses": value
      })

    else:
      return jsonify({"statuscode": 409, "message": "student not exists"})

  def post(self, studentId):
    args = stucourse.parse_args()
    course_id = args.get("course_id", None)
    course_name = args.get("course_name", None)
    course_instructor = args.get("course_instructor", None)
    term = args.get("term", None)

    user = StudentCourses.query.filter_by(student_id=studentId,
                                          course_id=course_id).first()
    if user:
      return jsonify({"statuscode": 500, "message": "Internal server error"})
    else:
      new_user = StudentCourses(student_id=studentId,
                                term=term,
                                course_id=course_id,
                                coursename=course_name,
                                course_instructor=course_instructor)
      db.session.add(new_user)
      db.session.commit()
      return jsonify({
          "statuscode": 201,
          "message": "Student courses created successfully"
      })


# /courses: courses api
courses = reqparse.RequestParser()
courses.add_argument("course_id")
courses.add_argument("course_name")
courses.add_argument("course_instructor")
courses.add_argument("term")


class CoursesAPI(Resource):

  def post(self):
    args = courses.parse_args()
    course_id = args.get("course_id", None)
    course_name = args.get("course_name", None)
    course_instructor = args.get("course_instructor", None)
    term = args.get("term", None)
    if course_id and course_name and course_instructor:
      course = Courses(course_id=course_id,
                       coursename=course_name,
                       course_instructor=course_instructor,
                       term=term)
      db.session.add(course)
      db.session.commit()
      return jsonify({
          "statuscode": 201,
          "message": "Course created successfully"
      })
    else:
      return jsonify({"statuscode": 409, "message": "missing fields"})


#/feedback/{studentId}/{course_id}:

stucour = reqparse.RequestParser()
stucour.add_argument("student_feedback")
stucour.add_argument("term")


class FeedbackAPI(Resource):

  def get(self, studentId, course_id):
    data = StudentCourses.query.filter_by(student_id=studentId,
                                          course_id=course_id).first()
    if data:
      return jsonify({
          "statuscode": 200,
          "course_id": course_id,
          "term_feedback": data.feedback
      })
    else:
      return jsonify({"statuscode": 409, "message": "course not exist"})

  def post(self, studentId, course_id):
    args = stucour.parse_args()
    term = args.get("term", None)
    feedback = args.get("student_feedback", None)
    feed = db.session.query(StudentCourses).filter(
        (StudentCourses.student_id == studentId)
        & (StudentCourses.course_id == course_id)).first()
    if feed:
      feed.feedback = feedback
      db.session.commit()
      return jsonify({
          "statuscode": 201,
          "message": "Feedback added successfully"
      })
    else:
      return jsonify({"statuscode": 409, "message": "course not exist"})


#  /learning_path/{studentId}:


class LearningPathAPI(Resource):

  def get(self, studentId):
    cour = User.query.filter_by(student_id=studentId).all()
    d = {
        "foundation": [
            "Computational Thinking", "Statistics for Data Science I",
            "Programming in Python", "English II",
            "Mathematics for Data Science I", "English I",
            "Mathematics for Data Science II", "Statistics for Data Science II"
        ],
        "diploma": [
            "Machine Learning Foundations ", "Tools in Data Science",
            "Database Management Systems",
            "Modern Application Development II ", "System Commands ",
            "Business Data Management ", "Machine Learning Techniques ",
            "Business Analytics ", "Programming Concepts using Java",
            "Modern Application Development I",
            "Programming, Data Structures and Algorithms using Python",
            "Machine Learning Practice",
            "Modern Application Development I - Project",
            "Modern Application Development II - Project",
            "Business Data Management - ProjectBusiness Data Management - Project",
            "Machine Learning Practice - Project"
        ],
        "degree": [
            "Software Testing ", "Software Engineering ",
            " AI: Search Methods for Problem Solving ", "Deep Learning",
            "Strategies for Professional Growth",
            "Algorithmic Thinking in Bioinformatics",
            "Big Data and Biological Networks",
            " Introduction to Cryptography and Cyber Security",
            "Data Visualization Design",
            "Special topics in Machine Learning (Reinforcement Learning)",
            "Thematic Ideas in Data Science", " Speech Technology",
            "Design Thinking for Data-Driven App Development", "Industry 4.0",
            "Sequential Decision Making", "Market Research",
            "Privacy & Security in Online Social Media",
            "Introduction to Big Data", "Financial Forensics",
            " Linear Statistical Models", "Advanced Algorithms",
            "Statistical Computing", "Computer Systems Design",
            "Programming in C", "Mathematical Thinking"
        ]
    }

    if cour:
      #temp = []
      #for i in cour:
      #  c = Courses.query.filter_by(course_id=i.course_id).first()
      #  temp.append(c.coursename)
      #if len(cour) <= 8:
      #  notcom = []
      #  for j in d["foundation"]:
      #    if j not in temp:
      #     notcom.append(j)
      return jsonify(
          {
              "learning_path1": [{
                  "term1": ["course1", "course2", "course3"]
              }, {
                  "term2": ["course1", "course2", "course3"]
              }]
          }, {
              "learning_path2": [{
                  "term1": ["course1", "course2", "course3"]
              }, {
                  "term2": ["course1", "course2", "course3"]
              }]
          }, {
              "learning_path3": [{
                  "term1": ["course1", "course2", "course3"]
              }, {
                  "term2": ["course1", "course2", "course3"]
              }]
          })

    return jsonify({"statuscode": 409, "message": "student not exists"})
    #return jsonify({"statuscode": 401, "message": "Access not possible"})
    #return jsonify({"statuscode": 500, "message": "Internal server error"})



class InstructorDashboardStatsAPI(Resource):

  def get(self, course_id, instructor_id):
    positive = 0
    feedba = StudentCourses.query.filter_by(course_id=course_id).all()
    if feedba:
      for feed in feedba:
        blob = TextBlob(feed.feedback)
        sentiment_polarity = blob.sentiment.polarity
        if sentiment_polarity > 0:
          positive += 1
      posiper = (len(feedba) / positive) * 100
      return jsonify({
          "statuscode": 200,
          "message": "feedback",
          "course_id": course_id,
          "Postitve_reviews_percentage": posiper,
      })
    else:
      return jsonify({"statuscode": 409, "message": "no feedbacks"})


#/feedback/{InstructorId}/{course_id}:


class InstructorFeedbackAPI(Resource):

  def get(self, InstructorId, course_id):
    data = StudentCourses.query.filter_by(course_id=course_id).all()
    if data:
      d = {}
      for row in data:
        try:
          d[row.term].append(row.feedback)
        except:
          d[row.term] = [row.feedback]
      return jsonify({"course_id": course_id, "term feedbacks": d})


#/notification
noti = reqparse.RequestParser()
noti.add_argument("message")
noti.add_argument("studentId")
noti.add_argument("email")


class NotificationAPI(Resource):

  def post(self):
    args = noti.parse_args()
    message = args.get("message", None)
    student_id = args.get("studentId", None)
    email = args.get("email", None)
    if message:
      return jsonify({"statuscode": 200, "message": "Notification sent"})
    else:
      return jsonify({"statuscode": 500, "message": "Internal server error"})
