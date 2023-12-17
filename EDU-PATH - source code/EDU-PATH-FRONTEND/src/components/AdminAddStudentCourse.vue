<template>
  <header class="d-flex justify-content-between align-items-center my-3 border">
    <h1 class="h3">Edu Path</h1>
  </header>
  <div>
    <h1>Admin </h1>
  </div>
  <div>
    <ul class="nav nav-pills nav-fill gap-2 p-1 small bg-primary rounded-5 shadow-sm" id="pillNav2" role="tablist" style="--bs-nav-link-color: var(--bs-white); --bs-nav-pills-link-active-color: var(--bs-primary); --bs-nav-pills-link-active-bg: var(--bs-white);">
      <li class="nav-item" role="presentation">
        <button class="nav-link rounded-5" id="student-tab2" data-bs-toggle="tab" type="button" role="tab" aria-selected="true"><a href="/addstudent" style="color: white;">Add Student</a></button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link rounded-5" id="course-tab2" data-bs-toggle="tab" type="button" role="tab" aria-selected="true"><a href="/addcourse" style="color: white;">Add Course</a></button>
      </li>
      <li class="nav-item" role="presentation">
         <button class="nav-link rounded-5" id="instructor-tab2" data-bs-toggle="tab" type="button" role="tab" aria-selected="true"><a href="/addinstructor" style="color: white;">Add Instructor</a> 
  </button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link active rounded-5" id="stats-tab2" data-bs-toggle="tab" type="button" role="tab" aria-selected="true"><a href="/addstudentcourse" style="color: black;">Stats</a></button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link rounded-5" id="stats-tab2" data-bs-toggle="tab" type="button" role="tab" ><a href="/accountcreation" style="color: white;">Account creation</a></button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link rounded-5" id="stats-tab2" data-bs-toggle="tab" type="button" role="tab" ><a href="/notification" style="color: white;">Notification</a></button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link rounded-5" id="stats-tab2" data-bs-toggle="tab" type="button" role="tab" ><a href="/addstudentmarks" style="color: white;">Add student marks</a></button>
      </li>
    </ul>
  </div>
   <br>
  <div>
     <h3><center> STATS</center></h3> 
  </div>
  <br>
  <section class="chart-info d-flex justify-content-between my-3 border">
    <div class="pie-chart">
      <!-- Placeholder for Pie Chart -->
      <canvas id="pieChart" width="200" height="200"></canvas>
    </div>
  </section>
</template>

<script>
  import Chart from 'chart.js/auto';
export default {
  name: 'AdminAddStudentCourse',
  data() {
  },
  methods: {
    adminaddstudentcourse() {
      // Add login functionality here
    }
  },
  mounted() {
    // Initialize Chart.js pie chart
    const ctxPie = document.getElementById('pieChart').getContext('2d');
    new Chart(ctxPie, {
      type: 'pie',
      data: {
        labels: ['Label 1', 'Label 2', 'Label 3'],
        datasets: [
          {
            data: [30, 40, 30], // Example data, replace with your own
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