<template>
  <header class="d-flex justify-content-between align-items-center my-3 border">
    <h1 class="h3">Edu Path</h1>
  </header>
  <div id="bod">
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
          <h2>{{ studentdetails.name }}</h2>
          <h2>{{ studentdetails.email }}</h2>
        </div>
        <div class="student">
          <p>Id : {{ studentdetails.id }}</p>
          <p>DOB : {{ studentdetails.dob }}</p>
          <p>Blood Group : {{ studentdetails.blood_group }}</p>
          <p>Gender : {{ studentdetails.gender }}</p>
          <p>Current Level : Degree</p>
          <p>Mobile Number : {{ studentdetails.mobile }}</p>
          <p>Address : {{ studentdetails.address }}</p>
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
    name: 'StudentDashboard',
    data() {
      return {
        items: ["Math1", "Statistics 1", "English1", "Computational Thinking", "Math2", "Statistic2", "English2", "Intro to Python", "MAD1", "JAVA", "MAD2", "DBMS", "System Commands", "PDSA", "MLF", "MLP", "MLT", "BDM", "BA", "TDS"],
        current : [],
        studentdetails : {
            "id": "21F3002478",
            "name": "Phani Kumar Jallipalli",
            "email": "21f3002478@study.iitm.ac.in",
            "gender": "M",
            "dob": "15/04/2000",
            "blood_group": "B+",
            "mobile": 8317566776,
            "address": "Eluru,Andhra pradesh"
          },
        studentcourses : [
          {
            "course_id": "001",
            "course_name": "Intro to bigbata",
            "course_instructor": "rangarajan",
            "term": "23T3"
          },
          {
            "course_id": "002",
            "course_name": "Software Engineering",
            "course_instructor": "rangarajan",
            "term": "23T3"
          },
          {
            "course_id": "003",
            "course_name": "SoftWare Testing",
            "course_instructor": "rangarajan",
            "term": "23T3"
          },
          {
            "course_id": "004",
            "course_name": "Strategies of professional Growth",
            "course_instructor": "rangarajan",
            "term": "23T3"
          },
          {
            "course_id": "001",
            "course_name": "Mlp",
            "course_instructor": "rangarajan",
            "term": "23T2"
          }
        ]
        }
    },
    async created() {
      for(var i=0;i<this.studentcourses.length; i++){
          if (this.studentcourses[i].term === "23T3"){
            this.current.push(this.studentcourses[i].course_name)
          }
          else{
            //push to another object to view completed courses
          }
        }
    },
    methods: {
      studentcourses() {
    }
  }
  };
</script>

<style>
  #grid {
    margin: 0;
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
    overflow: auto;
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
    padding-top: 10%;
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