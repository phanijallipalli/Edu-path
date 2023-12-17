<template>
  <header class="d-flex justify-content-between align-items-center my-3 border">
    <h1 class="h3">Edu Path</h1>
  </header>
  <div>
    <h1>Admin </h1>
  </div>
  <div>
    <ul class="nav nav-pills nav-fill gap-2 p-1 small bg-primary rounded-5 shadow-sm" id="pillNav2" role="tablist" style="--bs-nav-link-color: var(--bs-white); --bs-nav-pills-link-active-color: var(--bs-primary);--bs-nav-pills-link-active-bg: var(--bs-white);">
      <li class="nav-item" role="presentation">
        <button class="nav-link rounded-5" id="student-tab2" data-bs-toggle="tab" type="button" role="tab"  ><a href="/addstudent" style="color: white;">Add Student</a></button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link active rounded-5" id="course-tab2" data-bs-toggle="tab" type="button" role="tab" ><a href="/addcourse" style="color: black;">Add Course</a></button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link rounded-5" id="instructor-tab2" data-bs-toggle="tab" type="button" role="tab"><a href="/addinstructor" style="color: white;">Add Instructor</a></button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link rounded-5" id="stats-tab2" data-bs-toggle="tab" type="button" role="tab" ><a href="/addstudentcourse" style="color: white;">Stats</a></button>
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
       <h3><center> ADD COURSE </center></h3> 
  </div>
   <br>
  <div id="form">
  <form>
    <div class="mb-3">
      <label for="coursename" class="form-label">Course name</label>
      <input type="coursename" class="form-control" id="coursename">
    </div>
    <div class="mb-3">
      <label for="courseid" class="form-label">Course ID</label>
      <input type="courseid" class="form-control" id="courseid">
    </div>
    <div class="mb-3">
      <label for="term" class="form-label">Term</label>
      <input type="term" class="form-control" id="term">
    </div>
    <div class="mb-3">
      <label for="instructorid" class="form-label">Instructor ID</label>
      <input type="instructorid" class="form-control" id="instructorid">
    </div>
    <div class="mb-3">
      <label for="courseinstructors" class="form-label">Course Instructors</label>
      <input type="courseinstructors" class="form-control" id="courseinstructors">
    </div>   
    <center>
    <button type="submit" class="btn btn-primary">Submit</button></center>
    <br>
  </form>
  </div>
  <div>
    <center>
      <h5> Upload in bulk as csv file :   <button type="submit" class="btn btn-primary float-left">Upload</button>
    </h5>
    </center>  
  </div>
</template>

<script>
export default {
  name: 'AdminAddCourse',
  data() {
  },
  methods: {
    adminaddcourse() {
      // Add login functionality here
    }
  }
};
</script>

<style>
  #form{
    margin-left : 25%;
    margin-right : 25%;
  }
</style>