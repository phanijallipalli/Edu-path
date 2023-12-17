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
        <button class="nav-link active rounded-5" id="student-tab2" data-bs-toggle="tab" type="button" role="tab" aria-selected="true"><a href="/instdashboard" style="color: black;">Feedback</a></button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link rounded-5" id="course-tab2" data-bs-toggle="tab" type="button" role="tab" aria-selected="true"><a href="/InstructorStats" style="color: white;">Stats</a></button>
      </li>
    </ul>
  </div>
   <br>
  <div>
       <h3><center> Course Feedback </center></h3> 
  </div>
   <br>



    <div class="d-flex">
      <!-- Sidebar -->
      <div class="sidebar">
        <h2>Select Course</h2>
        <ul>
          <li v-for="course in courses" :key="course.id" @click="selectCourse(course.id)" :class="{ 'selected-course': course.id === selectedCourse }">
            {{ course.name }}
          </li>
        </ul>

        <h2>Sort By</h2>
        <select v-model="selectedSort">
          <option value="recent">Most Recent</option>
          <option value="top">Top Review</option>
          <option value="negative">Negative Feedback</option>
        </select>
      </div>

      <!-- Main Body -->
      <div class="main-body">
        <h2>Course Feedbacks</h2>
        <!-- Display course feedbacks based on selected course and sorting -->
        <template v-for="feedback in filteredFeedbacks">
          <div class="feedback">
            <p>{{ feedback.text }}</p>
            <p>Term: {{ feedback.term }}</p>
            <p>Posted on: {{ feedback.date }}</p>
          </div>
        </template>
      </div>
    </div>

</template>

<script>
export default {
  name: 'Feedbacks',
  data() {
    return {
      courses: [
        { id: 1, name: 'Math1' },
        { id: 2, name: 'Statistics 1' },
        // Add more courses as needed
      ],
      selectedCourse: null,
      selectedSort: 'recent',
      feedbacks: [
          { text: 'Great course!', rating: 5, date: '2023-01-01', courseId: 1, term: 1 },
          { text: 'Good content', rating: 4, date: '2023-01-05', courseId: 2, term: 2 },
          { text: 'Excellent instructor and engaging material!', rating: 5, date: '2023-02-10', courseId: 1, term: 1 },
          { text: 'The assignments were challenging but rewarding.', rating: 4, date: '2023-02-15', courseId: 2, term: 2 },
          { text: 'Really enjoyed the hands-on projects.', rating: 5, date: '2023-03-03', courseId: 1, term: 1 },
          { text: 'The course provided a solid foundation for the subject.', rating: 4, date: '2023-03-10', courseId: 2, term: 2 },
          { text: 'Interactive discussions made the learning experience enjoyable.', rating: 5, date: '2023-04-05', courseId: 1, term: 1 },
          { text: 'Clear explanations and helpful resources.', rating: 4, date: '2023-04-12', courseId: 2, term: 2 },
          { text: 'The course structure allowed for a gradual and thorough understanding.', rating: 5, date: '2023-05-02', courseId: 1, term: 1 },
          { text: 'Appreciated the real-world examples provided in the lectures.', rating: 4, date: '2023-05-10', courseId: 2, term: 2 },
          // Add more feedbacks with relevant information
      ],

    };
  },
  computed: {
    filteredFeedbacks() {
      // Filter feedbacks based on the selected course and sorting
      let filtered = this.feedbacks;
      if (this.selectedCourse) {
        filtered = filtered.filter(feedback => feedback.courseId === this.selectedCourse);
      }

      switch (this.selectedSort) {
        case 'recent':
          filtered.sort((a, b) => new Date(b.date) - new Date(a.date));
          break;
        case 'top':
          filtered.sort((a, b) => b.rating - a.rating);
          break;
        case 'negative':
          filtered = filtered.filter(feedback => feedback.rating < 3);
          break;
      }

      return filtered;
    },
  },
  methods: {
    selectCourse(courseId) {
      this.selectedCourse = courseId;
    },
  },
};
</script>

<style>
.sidebar {
  flex: 30%;
  padding: 20px;
  background-color: #f0f0f0;
}

.sidebar h2 {
  margin-bottom: 10px;
}

.sidebar ul {
  list-style: none;
  padding: 0;
}

.sidebar li {
  cursor: pointer;
  margin-bottom: 5px;
  padding: 5px;
  background-color: #e0e0e0;
}


  .sidebar li.selected-course {
    background-color: #336efd;
    color: white; /* You may adjust the text color for better visibility */
  }


.main-body {
  flex: 70%;
  padding: 20px;
}

.feedback {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
}
</style>
