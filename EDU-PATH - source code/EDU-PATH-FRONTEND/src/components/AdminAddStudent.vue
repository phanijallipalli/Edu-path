<template>
  <div>
    <header class="d-flex justify-content-between align-items-center my-3 border">
      <h1 class="h3">Edu Path</h1>
    </header>
    <h1>Admin </h1>
  </div>
  <div>
    <ul class="nav nav-pills nav-fill gap-2 p-1 small bg-primary rounded-5 shadow-sm" id="pillNav2" role="tablist" style="--bs-nav-link-color: var(--bs-white); --bs-nav-pills-link-active-color: var(--bs-primary); --bs-nav-pills-link-active-bg: var(--bs-white);">
      <li class="nav-item" role="presentation">
        <button class="nav-link active rounded-5" id="student-tab2" data-bs-toggle="tab" type="button" role="tab" aria-selected="true"><a href="/addstudent" style="color: black;">Add Student</a></button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link rounded-5" id="course-tab2" data-bs-toggle="tab" type="button" role="tab" aria-selected="true"><a href="/addcourse" style="color: white;">Add Course</a></button>
      </li>
      <li class="nav-item" role="presentation">
         <button class="nav-link rounded-5" id="instructor-tab2" data-bs-toggle="tab" type="button" role="tab" aria-selected="true"><a href="/addinstructor" style="color: white;">Add Instructor</a> 
</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link rounded-5" id="stats-tab2" data-bs-toggle="tab" type="button" role="tab" aria-selected="true"><a href="/addstudentcourse" style="color: white;">Stats</a></button>
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
       <h3><center> ADD STUDENT </center></h3> 
  </div>
   <br>
  <div id="form">
  <form>
    <div class="mb-3">
      <label for="studentname" class="form-label">Student name</label>
      <input type="studentname" class="form-control" id="studentname">
    </div>
    <div class="mb-3">
      <label for="studentid" class="form-label">Student ID</label>
      <input type="studentid" class="form-control" id="studentid">
    </div>
    <div class="mb-3">
      <label for="studentdob" class="form-label">Student Date of Birth</label>
      <input type="studentdob" class="form-control" id="studentdob">
    </div>
    <div class="mb-3">
      <label for="studentgender" class="form-label">Student Gender</label>
      <input type="studentgender" class="form-control" id="studentgender">
    </div>
    <div class="mb-3">
      <label for="studentmobilenumber" class="form-label">Student Mobile Number</label>
      <input type="studentmobilenumber" class="form-control" id="studentmobilenumber">
    </div>
    <div class="mb-3">
      <label for="parentmobilenumber" class="form-label">Parent Mobile number</label>
      <input type="parentmobilenumber" class="form-control" id="parentmobilenumber">
    </div>
    <div class="mb-3">
      <label for="studentbg" class="form-label">Student Blood Group</label>
      <input type="studentbg" class="form-control" id="studentbg">
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
  name: 'AdminAddStudent',
  data() {
  },
  methods: {
    adminaddstudent() {
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