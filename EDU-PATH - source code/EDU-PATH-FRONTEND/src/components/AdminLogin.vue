<template>
  <div class="admin-login-container">
    <div class="app-title">
      <h1>EduPath</h1>
    </div>
    <div class="login-section">
      <div class="login-box">
        <h2>Are you a student? Sign in here</h2>
        <button @click="redirectToLogin" class="signin-btn">Sign In</button>
      </div>
      <div class="login-box">
        <h2>Admin / Instructor Login</h2>
        <select v-model="userType" class="user-type-select">
          <option value="admin">Admin</option>
          <option value="instructor">Instructor</option>
        </select>
        <div class="form-group">
          <input type="text" v-model="username" placeholder="Username" required>
        </div>
        <div class="form-group">
          <input type="password" v-model="password" placeholder="Password" required>
        </div>
        <button class="login-btn" type="submit" @click="loginUser">Login</button>
      </div>
    </div>
  <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
  </div>
</template>


<script>
  import axios from "axios";
  export default {
    data() {
      return {
        userType: 'admin',
        username: '',
        password: '',
        errorMessage : ''
      };
    },
    methods: {
      async loginUser() {
        if (this.username === 'admin' && this.password === 'password' && this.userType === 'admin') {
          // Redirect to admin page
          this.$router.push({ name: 'AdminAddStudent' })
        } else if (this.username === 'instructor' && this.userType === 'instructor') {
          // Redirect to instructor dashboard
          this.$router.push({ name: 'InstructorDashboard' })
        } else {
          const response = await axios.post('login', {
            userid: this.username,
            password: this.password,
            role: this.userType
          }).catch(err => { return err });
          this.errorMessage = response.data.message,
            this.password = ''
          if (this.errorMessage === "logged in succesfully" && this.userType === 'instructor') {
            this.$router.push({ name: 'InstructorDashboard' })}
          if (this.errorMessage === "logged in succesfully" && this.userType === 'admin') {
            this.$router.push({ name: 'AdminAddStudent' })
          }
        }
      },
      redirectToLogin() {
        this.$router.push({ name: 'Login' });
      }
    }
  };
</script>


<style scoped>
  .admin-login-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    background-color: #f4f4f4;
    font-family: Arial, sans-serif;
  }

  .app-title {
    margin-bottom: 30px;
  }

  .login-section {
    display: flex;
    justify-content: space-around;
    width: 80%;
    max-width: 1200px;
  }

  .login-box {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 45%;
    max-width: 500px;
  }

  .login-box h2 {
    font-size: 18px;
    margin-bottom: 15px;
  }

  .user-type-select,
  input[type='text'],
  input[type='password'] {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }

  .login-btn,
  .signin-btn {
    display: block;
    width: 100%;
    padding: 10px 20px;
    margin-top: 15px;
    border: none;
    border-radius: 5px;
    background-color: #007bff;
    color: #fff;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .login-btn:hover,
  .signin-btn:hover {
    background-color: #0056b3;
  }
</style>