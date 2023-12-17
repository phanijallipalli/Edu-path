import pytest
import json
from flask import Flask
from flask.testing import FlaskClient
from flask_restful import Api
from app.model import User, StudentDetails, StudentCourses, Courses
from app.api import SignupAPI, LoginAPI, StudentDetailsAPI, db, StudentDetails, StudentCoursesAPI, CoursesAPI, InstructorDashboardStatsAPI, NotificationAPI, CoursesAPI, InstructorFeedbackAPI, FeedbackAPI, LearningPathAPI
# Create a test Flask application

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['TESTING'] = True
api = Api(app)
api.add_resource(SignupAPI, '/signup')
api.add_resource(LoginAPI, '/login')
api.add_resource(StudentDetailsAPI,
                 '/student_dasboard/student_details/<string:studentId>')
api.add_resource(NotificationAPI, "/notification")
api.add_resource(CoursesAPI, "/courses")
api.add_resource(
    InstructorFeedbackAPI,
    '/instructorfeedback/<string:InstructorId>/<string:course_id>')
api.add_resource(StudentCoursesAPI,
                 '/student_dasboard/student_courses/<string:studentId>')
api.add_resource(FeedbackAPI,
                 '/feedback/<string:studentId>/<string:course_id>')
api.add_resource(
    InstructorDashboardStatsAPI,
    '/instructor_dashboard/stats/<string:course_id>/<string:instructor_id>')

api.add_resource(LearningPathAPI, '/learning_path/<string:studentId>')
db.init_app(app)


@pytest.fixture
def client() -> FlaskClient:
  with app.test_client() as client:
    with app.app_context():
      db.create_all()
    yield client
    with app.app_context():
      db.session.remove()


def test_signup_success(client):
  data = {
      "userid": "test_user",
      "password": "test_password",
      "role": "student"
  }
  response = client.post('/signup', json=data)
  assert response.status_code == 200
  assert response.json['statuscode'] == 201
  assert response.json['message'] == "user created success"


def test_signup_username_exists(client):
  data = {
      "userid": "test_user",
      "password": "test_password",
      "role": "student"
  }
  response = client.post('/signup', json=data)
  assert response.status_code == 200
  assert response.json['statuscode'] == 409
  assert response.json['message'] == "username already exists"


def test_signup_internal_server_error(client):
  data = {"sid": "test_user", "password": None, "role": "student"}
  response = client.post('/signup', json=data)
  assert response.status_code == 200
  assert response.json['statuscode'] == 500
  assert response.json['message'] == "internal server error"


def test_login_success(client):
  data = {
      "userid": "test_user",
      "password": "test_password",
      "role": "student"
  }
  response = client.post('/login', json=data)
  assert response.status_code == 200
  assert response.json['statuscode'] == 200
  assert response.json['message'] == "logged in succesfully"


def test_login_role_doesnt_match(client):
  data = {"userid": "test_user", "password": "test_password", "role": "admin"}
  response = client.post('/login', json=data)
  assert response.status_code == 200
  assert response.json['statuscode'] == 200
  assert response.json['message'] == "role doesn't match"


def test_login_passwords_do_not_match(client):
  data = {
      "userid": "test_user",
      "password": "wrong_password",
      "role": "student"
  }
  response = client.post('/login', json=data)
  assert response.status_code == 200
  assert response.json['statuscode'] == 200
  assert response.json['message'] == "passwords doesn't match"


def test_login_user_not_found(client):
  data = {
      "userid": "nonexistent_user",
      "password": "test_password",
      "role": "student"
  }
  response = client.post('/login', json=data)
  assert response.status_code == 200
  assert response.json['statuscode'] == 200
  assert response.json['message'] == "user not found sign up"


def test_login_internal_server_error(client):
  data = {"userid": "test_user", "password": None, "role": "student"}
  response = client.post('/login', json=data)
  assert response.status_code == 200
  assert response.json['statuscode'] == 500
  assert response.json['message'] == "internal server error"


# Test cases for StudentDetailsAPI
def test_get_student_details_existing_student(client):
  with app.app_context():
    student = StudentDetails(student_id='123',
                             name='one two',
                             email='one.two@example.com',
                             gender='Male',
                             dob='1990-01-01',
                             blood_group='O+',
                             mobile='1234567890',
                             address='123 Main St')
    db.session.add(student)
    db.session.commit()

  response = client.get('/student_dasboard/student_details/123')
  assert response.status_code == 200
  assert response.json["statuscode"] == 200
  assert response.json["message"] == "student details"
  assert response.json["studentId"] == 123
  assert response.json["name"] == "one two"
  assert response.json["email"] == "one.two@example.com"
  assert response.json["gender"] == "Male"
  assert response.json["dob"] == "1990-01-01"
  assert response.json["blood_group"] == "O+"
  assert response.json["mobile"] == "1234567890"
  assert response.json["address"] == "123 Main St"


def test_get_student_details_nonexistent_student(client):
  # Assuming there is no student with ID '456'
  response = client.get('/student_dasboard/student_details/456')
  assert response.status_code == 200
  assert response.json == {
      "statuscode": 500,
      "message": "student not exist access not possible"
  }


def test_create_new_student(client):
  data = {
      "name": "new_student",
      "email": "new_student@example.com",
      "mobile": "9876543210",
      "address": "new Main St",
      "dob": "2000-01-01",
      "gender": "female",
      "blood_group": "A+"
  }
  response = client.post('/student_dasboard/student_details/1234',
                         data=json.dumps(data),
                         content_type='application/json')
  assert response.status_code == 200
  assert response.json['statuscode'] == 201
  assert response.json['message'] == "Student created successfully"


def test_create_existing_student(client):
  data = {
      "name": "one_two",
      "email": "one.two@example.com",
      "mobile": "1234567890",
      "address": "123 Main St",
      "dob": "1990-01-01",
      "gender": "Male",
      "blood_group": "O+"
  }

  response = client.post('/student_dasboard/student_details/1234',
                         data=json.dumps(data),
                         content_type='application/json')

  assert response.status_code == 200
  assert response.json['statuscode'] == 409
  assert response.json['message'] == "Student details already exists"


def test_update_student_details(client):
  # Update the student details
  updated_student_data = {
      "name": "one two_updated",
      "email": "one.two_updated@example.com",
      "mobile": "9876543210",
      "address": "123 Updated St",
      "dob": "2000-02-02",
      "gender": "Female",
      "blood_group": "B-"
  }
  response = client.put('/student_dasboard/student_details/123',
                        json=updated_student_data)
  assert response.status_code == 200
  assert response.json['message'] == "Student details updated successfully"


def test_update_nonexistent_student_details(client):
  # Attempt to update details for a non-existent student
  updated_student_data = {
      "name": "John Updated",
      "email": "john.updated@example.com",
      "mobile": "9876543210",
      "address": "456 Updated St",
      "dob": "2000-02-02",
      "gender": "Female",
      "blood_group": "B-"
  }
  response = client.put('/student_dasboard/student_details/456',
                        json=updated_student_data)
  assert response.status_code == 200
  assert response.json == {
      "statuscode": 204,
      "message": "student data not exists"
  }


def test_create_course(client):
  # Test creating a new course
  data = {
      "course_id": "new_course",
      "course_name": "Python",
      "course_instructor": "Prof. Python",
      "term": "jan 2023"
  }

  response = client.post('/courses', json=data)

  assert response.status_code == 200
  assert response.json['statuscode'] == 201
  assert response.json['message'] == 'Course created successfully'


def test_create_course_missing_fields(client):
  # Test creating a new course with missing fields
  data = {
      "course_name": "Python",
      "course_instructor": "Prof. Python",
      "term": "jan 2023"
  }

  response = client.post('/courses', json=data)

  assert response.status_code == 200
  assert response.json['statuscode'] == 409
  assert response.json['message'] == 'missing fields'


def test_create_student_courses(client):
  # Test creating new student courses
  data_courses = {
      "course_id": "new_course",
      "course_name": "Python",
      "course_instructor": "Prof. Python",
      "term": "jan 2023"
  }

  response = client.post('/student_dasboard/student_courses/123',
                         data=json.dumps(data_courses),
                         content_type='application/json')

  #assert response.status_code == 201
  assert response.json['statuscode'] == 201
  assert response.json['message'] == 'Student courses created successfully'


def test_get_student_courses(client):

  # Test getting student courses
  response = client.get('/student_dasboard/student_courses/123')

  assert response.status_code == 200
  assert response.json['statuscode'] == 200
  assert response.json['message'] == 'student courses'
  assert response.json['courses'] != {}


def test_get_nonexistent_student_courses(client):
  # Test getting courses for a non-existent student
  response = client.get('/student_dasboard/student_courses/nonexistent_user')

  assert response.status_code == 200
  assert response.json['statuscode'] == 409
  assert response.json['message'] == 'student not exists'


def test_post_feedback(client):
  student_id = "123"
  course_id = "new_course"
  data = {
      "term": "jan 2023",
      "student_feedback": "Great course! Enjoyed the content."
  }
  response = client.post('/feedback/123/new_course', json=data)
  assert response.status_code == 200
  assert response.json['statuscode'] == 201
  assert response.json['message'] == 'Feedback added successfully'


def test_get_feedback(client):
  student_id = "123"
  course_id = "new_course"
  response = client.get('/feedback/123/new_course')
  assert response.status_code == 200
  assert response.json['statuscode'] == 200
  assert response.json['term_feedback'] == 'Great course! Enjoyed the content.'
  assert response.json['course_id'] == 'new_course'


def test_get_feedback_nonexistent_course(client):
  student_id = "123"
  course_id = "dummy_course"
  response = client.get('/feedback/123/dummy_course')
  assert response.status_code == 200
  assert response.json['statuscode'] == 409
  assert response.json['message'] == 'course not exist'


def test_post_feedback_non_existing_course(client):
  student_id = "123"
  course_id = "existing_course"
  data = {"term": "may 2023", "feedback": "Great course! Enjoyed the content."}
  response = client.post('/feedback/123/course_123', json=data)
  assert response.status_code == 200
  assert response.json['statuscode'] == 409
  assert response.json['message'] == 'course not exist'


def test_instructor_dashboard_stats_api(client):
  feedback_data = {
      'course_id': 'new_course',
      'feedback': 'Great course! Enjoyed the content.',
      'term': 'may 2023'
  }
  response = client.get(
      '/instructor_dashboard/stats/new_course/instructor_123')
  assert response.status_code == 200
  assert response.json['statuscode'] == 200
  assert response.json['message'] == 'feedback'
  assert response.json['course_id'] == 'new_course'
  assert response.json['Postitve_reviews_percentage'] == 100.0


def test_instructor_dashboard_stats_api_no_feedback(client):
  response = client.get(
      '/instructor_dashboard/stats/test_course/test_instructor')
  assert response.status_code == 200
  assert response.json['statuscode'] == 409
  assert response.json['message'] == 'no feedbacks'


def test_instructor_feedback_api_with_feedback(client):
  feedback_data = {
      'course_id': 'new_course',
      'feedback': 'Great course! Enjoyed the content.',
      'term': 'jan 2023'
  }
  response = client.get('/instructorfeedback/instructor_123/new_course')
  assert response.status_code == 200
  assert response.json['course_id'] == 'new_course'
  assert response.json['term feedbacks']['jan 2023'][
      0] == 'Great course! Enjoyed the content.'


def test_notification_api_successful(client):
  # Test with valid data
  notification_data = {
      'message': 'New notification',
      'studentId': '123',
      'email': 'one.two@example.com'
  }
  response = client.post('/notification',
                         data=json.dumps(notification_data),
                         content_type='application/json')
  assert response.status_code == 200
  assert response.json['statuscode'] == 200
  assert response.json['message'] == 'Notification sent'


def test_notification_api_missing_data(client):
  notification_data = {
      'studentId': 'test_student',
      'email': 'test@example.com'
  }
  response = client.post('/notification',
                         data=json.dumps(notification_data),
                         content_type='application/json')
  assert response.status_code == 200
  assert response.json['statuscode'] == 500
  assert response.json['message'] == 'Internal server error'
