import { createRouter, createWebHistory } from 'vue-router'
import AdminAddCourse from "../components/AdminAddCourse.vue"
import AdminAddInstructor from "../components/AdminAddInstructor.vue"
import AdminAddStudent from "../components/AdminAddStudent.vue"
import AdminAddStudentCourse from "../components/AdminAddStudentCourse.vue"
import InstructorDashboard from "../components/InstructorDashboard.vue"
import InstructorStatistics from "../components/InstructorStatistics.vue"
import Login from "../components/Login.vue"
import StudentCourses from "../components/StudentCourses.vue"
import StudentDashboard from "../components/StudentDashboard.vue"
import StudentFeedback from "../components/StudentFeedback.vue"
import StudentRecommendation from "../components/StudentRecommendation.vue"
import StudentCourseFeedback from "../components/StudentCoursefeedback.vue"
import AdminLogin from "../components/AdminLogin.vue"
import Notification from "../components/Notification.vue"
import AccountCreation from "../components/Accountcreation.vue"
import Addstudentmarks from "../components/AddStudentMarks.vue"

const routes = [
  { path: "/addcourse", component: AdminAddCourse },
  { path: "/addinstructor", component: AdminAddInstructor },
  { path: "/addstudent", component: AdminAddStudent, name: "AdminAddStudent" },
  { path: "/addstudentcourse", component: AdminAddStudentCourse },
  { path: "/instdashboard", component: InstructorDashboard, name: "InstructorDashboard" },
  { path: "/InstructorStats", component: InstructorStatistics },
  { path: "/", component: Login, name: "Login" },
  { path: "/studentcourses", component: StudentCourses },
  { path: "/studentdashboard", component: StudentDashboard },
  { path: "/studentfeedback", component: StudentFeedback },
  { path: "/studentreccomdation", component: StudentRecommendation },
  { path: "/studentcoursefeedback", component: StudentCourseFeedback },
  { path: "/AdminLogin", component: AdminLogin, name: "AdminLogin" },
  { path: "/notification", component: Notification, name: "Notification" },
  { path: "/accountcreation", component: AccountCreation, name: "AccountCreation" },
  { path: "/addstudentmarks", component: Addstudentmarks, name: "Addstudentmarks" },
]

const router = createRouter({
  history: createWebHistory('/'), // Provide a fallback value
  routes
});

export default router