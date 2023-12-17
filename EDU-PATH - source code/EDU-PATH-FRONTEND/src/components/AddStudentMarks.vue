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
        <button class="nav-link rounded-5" id="course-tab2" data-bs-toggle="tab" type="button" role="tab" ><a href="/addcourse" style="color: white;">Add Course</a></button>
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
        <button class="nav-link active rounded-5" id="stats-tab2" data-bs-toggle="tab" type="button" role="tab" ><a href="/addstudentmarks" style="color: black;">Add student marks</a></button>
      </li>
    </ul>
  </div>
   <br>
  <div>
       <h3><center> Account Creation </center></h3> 
  </div>
   <br>
  <div id="form">
  <form>
    <div class="mb-3">
       <center>
      <label for="coursename" class="form-label">Assignment :   </label>
    <select v-model="Assignment" class="user-type-select">
      <option value="Assignment 1">Assignment 1</option>
      <option value="Assignment 2">Assignment 2</option>
      <option value="Assignment 3">Assignment 3</option>
      <option value="Assignment 4">Assignment 4</option>
      <option value="Assignment 5">Assignment 5</option>  
      <option value="Assignment 6">Assignment 6</option>
      <option value="Assignment 7">Assignment 7</option>
      <option value="Assignment 8">Assignment 8</option>
      <option value="Assignment 9">Assignment 9</option>
      <option value="Assignment 10">Assignment 10</option>
      <option value="Assignment 11">Assignment 11</option>
      <option value="Assignment 12">Assignment 12</option>
      <option value="Quiz 1">Quiz 1</option>
      <option value="Quiz 2">Quiz 2</option>
      <option value="End term">End term</option>
    </select>
      </center>
    </div>
    <div class="mb-3">
        <label for="userid" class="form-label">User Id</label>
        <input type="userid" class="form-control" id="Userid">
      </div>
    <div class="mb-3">
      <label for="courseid" class="form-label">Course id</label>
      <input type="courseid" class="form-control" id="courseid">
    </div>
    <div class="mb-3">
      <label for="coursemarks" class="form-label">Marks</label>
      <input type="coursemarks" class="form-control" id="courseid">
    </div>
    <center>
    <button type="submit" class="btn btn-primary">Submit</button></center>
    <br>
  </form>
  </div>
  <div> 
  </div>
</template>

<script>
export default {
  name: 'AccountCreation',
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