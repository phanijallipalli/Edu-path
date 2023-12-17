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
        <button class="nav-link active rounded-5" id="stats-tab2" data-bs-toggle="tab" type="button" role="tab" ><a href="/notification" style="color: black;">Notification</a></button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link rounded-5" id="stats-tab2" data-bs-toggle="tab" type="button" role="tab" ><a href="/addstudentmarks" style="color: white;">Add student marks</a></button>
      </li>
    </ul>
  </div>
   <br>
  <div>
       <h3><center> Notification </center></h3> 
  </div>
   <br>
  <div id="form">
  <form @submit.prevent="sendnotfication">
    <div class="mb-3">
      <label for="coursename" class="form-label">This message will sent to all students </label>
      <textarea type="id" class="form-control" id="exampleInputid1" v-model="message" required >Type Message here </textarea>
    </div>  
    <center>
    <button type="submit" class="btn btn-primary">Submit</button></center>
    <br>
  </form>
  </div>
  <div> 
    <center><div v-if="errorMessage" class="error-message">{{ errorMessage }}</div></center>
  </div>
</template>

<script>
  import axios from "axios";
export default {
  name: 'Notification',
  data() {
    return{
      errorMessage : "",
      message : ""
    }
  },
  methods: {
      async sendnotfication() {
        const response = await axios.post('notification', {
            message : this.message
        }).catch(err => { return err });
        this.errorMessage = response.data.message,
        this.message = ""
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