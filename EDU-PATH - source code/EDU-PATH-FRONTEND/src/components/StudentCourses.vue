<template>
  <header class="d-flex justify-content-between align-items-center my-3 border">
    <h1 class="h3">Edu Path</h1>
  </header>
  <div>
    <div id="Navbar">
      <ul class="nav nav-pills nav-fill gap-2 p-1 small bg-primary rounded-5 shadow-sm" id="pillNav2" role="tablist"
        style="--bs-nav-link-color: var(--bs-white); --bs-nav-pills-link-active-color: var(--bs-dark); --bs-nav-pills-link-active-bg: var(--bs-white);">
        <li class="nav-item" role="presentation">
          <button class="nav-link active rounded-5" id="student-tab2" data-bs-toggle="tab" type="button" role="tab"
            aria-selected="true"><a href="/studentdashboard" style="color: black;">Dashboard</a></button>
        </li>
        <li class="nav-item" role="presentation">
          <button class="nav-link rounded-5" id="course-tab2" data-bs-toggle="tab" type="button" role="tab"
            aria-selected="true"><a href="/studentfeedback" style="color: white;">Feedbacks</a></button>
        </li>
        <li class="nav-item" role="presentation">
          <button class="nav-link rounded-5" id="instructor-tab2" data-bs-toggle="tab" type="button" role="tab"
            aria-selected="true"><a href="/studentreccomdation" style="color: white;">Recommendation Paths</a></button>
        </li>
      </ul>
    </div>
    <div id="grid">
      <div class="left-column">
        <div class="details">
          <h2>Course Name</h2>
          <h2>Instructor Name</h2>
        </div>
        <div class="student">
          <template v-for="(value, item) in student_marks.Marks[0]" :key="item">
            <p>{{ item }} {{ value }}</p>
          </template>
        </div>
      </div>
      <div class="right-column">
        <div>
          <div class="top-row">
            <h2>Current Courses</h2>
            <template v-for="item in current" :key="item">
              <div class="course">
                <a href="/studentcourses"> {{ item }} </a>
                <a href="/studentfeedback" style="color: blue;"> feedback</a>
              </div>
            </template>
          </div>
          <div class="bottom-row">
            <h2>Completed Courses</h2>
            <template v-for="item in items" :key="item">
              <div class="course">
                <a href="/studentcourses"> {{ item }} </a>
                <a href="/studentfeedback" style="color: blue;"> feedback</a>
              </div>
            </template>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'StudentCourses',
    data() {
      return {
        items: ["Math1", "Statistics 1", "English1", "Computational Thinking", "Math2", "Statistic2", "English2", "Intro to Python", "MAD1", "JAVA", "MAD2", "DBMS", "System Commands", "PDSA", "MLF", "MLP", "MLT", "BDM", "BA", "TDS"],
        current: ["Intro to Bigdata", "Software Testing", "Software Engineering", "Strategies of Professional Growth"],
        student_marks : {
            "Course_id": "course id",
            "instructor_id": "instructor id",
            "Marks": [
              {
                "assignment 1": 100,
                "assignment 2": 100,
                "assignment 3": 100,
                "assignment 4": 100,
                "assignment 5": 100,
                "assignment 6": 100,
                "assignment 7": 100,
                "assignment 8": 100,
                "assignment 9": 100,
                "assignment 10": 100,
                "assignment 11": 100,
                "assignment 12": 100,
                "Quiz 1": 100,
                "Quiz 2": 100,
                "Endterm": 100,
                "Total marks": 100,
                "coursegrade": "S"
              }
            ]
          }
      }
    },
    methods: {
      studentcourses() {
        // Add login functionality here
      }
    }
  };
</script>

<style>
  #grid {
    margin: 0;
    height: 100vh;
    /* Set the height of the grid to the full viewport height */
    display: flex;

  }

  #Navbar {
    margin-top: 1%;
    margin-bottom: 1%;
    font-size: 125%;
  }

  .left-column,
  .right-column {
    box-sizing: border-box;
    padding: 20px;
    height: 100%;
  }

  .details {
    padding-top: 5%;
    text-align: center;
    font-size: 150%;
  }

  .student {
    padding-left: 10%;
    font-size: 120%;
    padding-top: 5%;
  }

  .left-column {
    background-color: #f0f0f0;
    /* Change this to your desired color */
    flex: 30%;
  }

  .right-column {
    background-color: #e0e0e0;
    /* Change this to your desired color */
    flex: 70%;
  }

  .top-row {
    background-color: #f0f0f0;
    /* Change this to your desired color */
    flex: 30%;
    padding-top: 2%;
    padding-left: 5%;
    padding-bottom: 2%;
    font-size: 120%;
  }

  .bottom-row {
    background-color: #e0e0e0;
    /* Change this to your desired color */
    flex: 70%;
    padding-top: 2%;
    padding-left: 5%;
    padding-bottom: 2%;
    font-size: 120%;
  }

  a {
    text-decoration: none;
    color: black;
  }

  .course {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 50px;
    /* Set the height of the container */
    padding: 0 20px;
    /* Add some padding for spacing */
  }
</style>