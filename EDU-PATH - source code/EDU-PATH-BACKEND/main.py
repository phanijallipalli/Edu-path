from app import app
from app import api

from app.api import SignupAPI, LoginAPI, StudentDetailsAPI, db, StudentDetails, StudentCoursesAPI, CoursesAPI, InstructorDashboardStatsAPI, NotificationAPI, CoursesAPI, InstructorFeedbackAPI, FeedbackAPI, LearningPathAPI

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

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
