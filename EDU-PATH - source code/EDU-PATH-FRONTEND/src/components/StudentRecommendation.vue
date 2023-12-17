<template>
  <header class="d-flex justify-content-between align-items-center my-3 border">
    <h1 class="h3">Edu Path</h1>
  </header>
  <div>
    <div id="Navbar">
      <ul class="nav nav-pills nav-fill gap-2 p-1 small bg-primary rounded-5 shadow-sm" id="pillNav2" role="tablist"
        style="--bs-nav-link-color: var(--bs-white); --bs-nav-pills-link-active-color: var(--bs-dark); --bs-nav-pills-link-active-bg: var(--bs-white);">
        <li class="nav-item" role="presentation">
          <button class="nav-link rounded-5" id="student-tab2" data-bs-toggle="tab" type="button" role="tab"
            aria-selected="true"><a href="/studentdashboard" style="color: white;">Dashboard</a></button>
        </li>
        <li class="nav-item" role="presentation">
          <button class="nav-link rounded-5" id="course-tab2" data-bs-toggle="tab" type="button" role="tab"
            aria-selected="true"><a href="/studentfeedback" style="color: white;">Feedbacks</a></button>
        </li>
        <li class="nav-item" role="presentation">
          <button class="nav-link active rounded-5" id="instructor-tab2" data-bs-toggle="tab" type="button" role="tab"
            aria-selected="true"><a href="/studentreccomdation" style="color: black;">Recommendation Paths</a></button>
        </li>
      </ul>
    </div>
  </div>
  <h1>Recommendation Paths</h1>
  <div class="grid-container">
    <template v-for="(value,key) in learningpath" :key="key">
      <div class="grid-item">
        <template v-for="(path,learning) in value" :key="value">
          <h2> {{ learning }} </h2>
          <template v-for="(courses,term) in path" :key="courses">
            <template v-for="(indicourses,name) in courses" :key="courses">
              <h2> {{ name }} - {{ indicourses.join(",") }} </h2>
            </template>
          </template>
        </template>
      </div>
    </template>
  </div>
</template>

<script>
  export default {
    name: 'StudentRecommendation',
    data() {
      return {
        Recommemdations: [], //['Data Science + Machine Learning + Artificial Intelligence', 'Cyber Security + Data Analytics', 'Cloud Computing + Cyber Security + Data Forensics'],
        learningpath: [
          {
            "learning_path1": [
              {
                "term1": [
                  "course1",
                  "course2",
                  "course3"
                ]
              },
              {
                "term2": [
                  "course1",
                  "course2",
                  "course3"
                ]
              }
            ]
          },
          {
            "learning_path2": [
              {
                "term1": [
                  "course1",
                  "course2",
                  "course3"
                ]
              },
              {
                "term2": [
                  "course1",
                  "course2",
                  "course3"
                ]
              }
            ]
          },
          {
            "learning_path3": [
              {
                "term1": [
                  "course1",
                  "course2",
                  "course3"
                ]
              },
              {
                "term2": [
                  "course1",
                  "course2",
                  "course3"
                ]
              }
            ]
          }
        ]
      }
    },
    created() {
      this.learningpath
    },
    methods: {
      studentrecommendation() {
        // Add login functionality here
      }
    }
  };
</script>

<style>
  .grid-container {
    display: grid;
    gap: 10px;
    /* Adjust the gap between items */
  }

  .grid-item {
    border: 1px solid #ccc;
    padding: 1px;
    background-color: #f0f0f0;
  }
</style>