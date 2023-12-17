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
          <button class="nav-link active rounded-5" id="course-tab2" data-bs-toggle="tab" type="button" role="tab"
            aria-selected="true"><a href="/studentfeedback" style="color: black;">Feedbacks</a></button>
        </li>
        <li class="nav-item" role="presentation">
          <button class="nav-link rounded-5" id="instructor-tab2" data-bs-toggle="tab" type="button" role="tab"
            aria-selected="true"><a href="/studentreccomdation" style="color: white;">Recommendation Paths</a></button>
        </li>
      </ul>
    </div>
  </div>
  <div id="grid">
      <div class="left-column">
        <div class="details">
          <h2>Course Name</h2>
          <h2>Course Instructor</h2>
        </div>
        <div class="student">
          <template v-for="item in terms" :key="item">
            <div class="student">
              <a href="/studentcoursefeedback"> {{ item }} </a>
            </div>
          </template>
        </div>
      </div>
      <div class="right-column">
        <div>
          <div class="top-row">
            <h2>Your Feedback</h2>
            <div class="mb-3">
                <textarea type="id" class="form-control" id="exampleInputid1">submit your feedback here </textarea>
              </div>
            <center><button type="submit" class="btn btn-primary">Submit</button></center>
          </div>
          <div class="bottom-row">
            <h2>Term Name - Feedbacks</h2>
            <template v-for="item in feedbacks" :key="item">
                <p> {{ item }} </p>
            </template>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: 'StudentCourseFeedback',
  data() {
    return {
      terms: ["21-TERM1", "21-TERM2", "21-TERM3", "22-TERM1", "22-TERM2", "22-TERM3", "23-TERM1", "23-TERM2", "23-TERM3"],
      feedbacks: ["Great job! Very satisfied with the service.",
        "The product exceeded my expectations. Thank you!",
        "Good experience overall. A few improvements can be made.",
        "Not happy with the customer support. It took too long to get a response.",
        "Excellent service! Will definitely recommend to others.",
        "The quality of the product is outstanding.",
        "Fast shipping and delivery. Impressed with the efficiency.",
        "Average experience. Room for improvement.",
        "The website interface is user-friendly. Easy to navigate.",
        "Prompt and helpful customer support.",
        "Satisfied with the purchase. Good value for money.",
        "The product arrived in perfect condition. No complaints.",
        "Great customer service. Resolved my issue quickly.",
        "Impressed with the variety of products available.",
        "Timely updates on the order status. Smooth process.",
      ]
    }
  },
  methods: {
    studentcoursefeedback() {
      // Add login functionality here
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
    text-align: center;
    font-size : 100%;
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
    padding-right : 5%;
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