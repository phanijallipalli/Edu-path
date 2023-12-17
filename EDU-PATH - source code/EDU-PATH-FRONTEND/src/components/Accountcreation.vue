<template>
  <header class="d-flex justify-content-between align-items-center my-3 border">
    <h1 class="h3">Edu Path</h1>
  </header>
  <div>
    <h1>Admin </h1>
  </div>
  <div>
    <ul class="nav nav-pills nav-fill gap-2 p-1 small bg-primary rounded-5 shadow-sm" id="pillNav2" role="tablist"
      style="--bs-nav-link-color: var(--bs-white); --bs-nav-pills-link-active-color: var(--bs-primary);--bs-nav-pills-link-active-bg: var(--bs-white);">
      <li class="nav-item" role="presentation">
        <button class="nav-link rounded-5" id="student-tab2" data-bs-toggle="tab" type="button" role="tab"><a
            href="/addstudent" style="color: white;">Add Student</a></button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link rounded-5" id="course-tab2" data-bs-toggle="tab" type="button" role="tab"><a
            href="/addcourse" style="color: white;">Add Course</a></button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link rounded-5" id="instructor-tab2" data-bs-toggle="tab" type="button" role="tab"><a
            href="/addinstructor" style="color: white;">Add Instructor</a></button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link rounded-5" id="stats-tab2" data-bs-toggle="tab" type="button" role="tab"><a
            href="/addstudentcourse" style="color: white;">Stats</a></button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link active rounded-5" id="stats-tab2" data-bs-toggle="tab" type="button" role="tab"><a
            href="/accountcreation" style="color: black;">Account creation</a></button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link rounded-5" id="stats-tab2" data-bs-toggle="tab" type="button" role="tab"><a
            href="/notification" style="color: white;">Notification</a></button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link rounded-5" id="stats-tab2" data-bs-toggle="tab" type="button" role="tab"><a
            href="/addstudentmarks" style="color: white;">Add student marks</a></button>
      </li>
    </ul>
  </div>
  <br>
  <div>
    <h3>
      <center> Account Creation </center>
    </h3>
  </div>
  <br>
  <div id="form">
    <form @submit.prevent="accountcreation">
      <div class="mb-3">
        <center>
          <label for="coursename" class="form-label">User Type : </label>
          <select v-model="userType" class="user-type-select">
            <option value="admin">Admin</option>
            <option value="instructor">Instructor</option>
            <option value="student">Student</option>
          </select>
        </center>
      </div>
      <div class="mb-3">
        <label for="userid" class="form-label">User Id</label>
        <input type="userid" class="form-control" id="Userid" v-model="userid" required>
      </div>
      <div class="mb-3">
        <label for="userpassword" class="form-label">User Password</label>
        <input type="userpassword" class="form-control" id="Userpassword" v-model="password" required>
      </div>
      <center>
        <button type="submit" class="btn btn-primary">Submit</button>
      </center>
      <br>
    </form>
  </div>
  <div>
    <center>
      <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
    </center>
  </div>
</template>

<script>
  import axios from "axios";
  export default {
    name: 'AccountCreation',
    data() {
      return {
        userType: '',
        userid: '',
        password: '',
        errorMessage: '',
      };
    },
    methods: {
      async accountcreation() {
        if (this.userType !== "") {
          const response = await axios.post('signup', {
            userid: this.userid,
            password: this.password,
            role: this.userType
          }).catch(err => { return err });
          this.errorMessage = response.data.message,
            this.userType = '',
            this.userid = '',
            this.password = ''
        }
    else{
        this.errorMessage = "Select role"
      }
    }
    }
  };
</script>

<style>
  #form {
    margin-left: 25%;
    margin-right: 25%;
  }
</style>