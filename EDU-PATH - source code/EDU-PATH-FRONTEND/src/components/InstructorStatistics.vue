<template>
<div>
  <header class="d-flex justify-content-between align-items-center my-3 border">
    <h1 class="h3">Edu Path</h1>
  </header>
  <h1>Instructor </h1>
</div>
<div>
  <ul class="nav nav-pills nav-fill gap-2 p-1 small bg-primary rounded-5 shadow-sm" id="pillNav2" role="tablist" style="--bs-nav-link-color: var(--bs-white); --bs-nav-pills-link-active-color: var(--bs-primary); --bs-nav-pills-link-active-bg: var(--bs-white);">

    <li class="nav-item" role="presentation">
      <button class="nav-link rounded-5" id="course-tab2" data-bs-toggle="tab" type="button" role="tab" aria-selected="true"><a href="/instdashboard" style="color: white;">Feedback</a></button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link active rounded-5" id="student-tab2" data-bs-toggle="tab" type="button" role="tab" aria-selected="true"><a href="/InstructorStats" style="color: black;">Stats</a></button>
    </li>
  </ul>
</div>
 <br>
<div>
     <h3><center> Course Feedback </center></h3> 
</div>



    <section class="course-info my-3 border">
      <h2 class="h4">{{ courseTitle }}</h2>
      <p>{{ instructor }}</p>
    </section>
    <section class="score-info d-flex justify-content-between my-3 border">
      <div class="average-score">Average Score: {{ averageScore }}</div>
      <div class="min-score">Minimum Score: {{ minScore }}</div>
      <div class="top-review">Top Review: {{ topReview }}</div>
    </section>
    <section class="student-info d-flex justify-content-between my-3 border">
      <div class="registered-students">Registered Students: {{ registeredStudents }}</div>
      <div class="average-students">Average Students: {{ averageStudents }}</div>
      <div class="max-students">Maximum Students: {{ maxStudents }}</div>
    </section>
  <!--
    <section class="feedback-info d-flex justify-content-between my-3 border">
      <div class="feedback-ratio">Feedback Ratio: {{ feedbackRatio }}</div>
      <div class="difficulty">Difficulty: {{ difficulty }}</div>
    </section> -->
    <section class="chart-info d-flex justify-content-between my-3 border">
      <div class="pie-chart">
        <!-- Placeholder for Pie Chart -->
        <canvas id="pieChart" width="200" height="200"></canvas>
      </div>
      <div class="bar-graph">
        <!-- Bootstrap Progress Bar (Bar Graph) -->
        <div class="progress" style="height: 150px;">
          <div
            class="progress-bar"
            role="progressbar"
            :style="{ width: averageScore }"
            aria-valuenow="50"
            aria-valuemin="0"
            aria-valuemax="100"
          >
            {{ averageScore }}
          </div>
        </div>
      </div>
    </section>

</template>

<script>
import Chart from 'chart.js/auto';

export default {
  data() {
    return {
      courseTitle: 'Maths 1',
      instructor: 'Mr.XYZ',
      averageScore: '50%', // Assuming averageScore is a percentage (e.g., '50%')
      minScore: '45',
      topReview: '98',
      registeredStudents: '20138',
      averageStudents: '4502',
      maxStudents: '5032',
      feedbackRatio: 'Feedback Ratio Placeholder',
      difficulty: 'Difficulty Placeholder',
    };
  },
  mounted() {
    // Initialize Chart.js pie chart
    const ctxPie = document.getElementById('pieChart').getContext('2d');
    new Chart(ctxPie, {
      type: 'pie',
      data: {
        labels: ['Positive', 'Negative', 'Neutral'],
        datasets: [
          {
            data: [60, 10, 30], // Example data, replace with your own
            backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56'], // Example colors
          },
        ],
      },
    });
  },
};
</script>

<style scoped>
.container {
  background-color: #f0f0f0;
  padding: 15px;
}

.border {
  border: 1px solid #ddd;
  padding: 10px;
  background-color: #fff;
}
</style>