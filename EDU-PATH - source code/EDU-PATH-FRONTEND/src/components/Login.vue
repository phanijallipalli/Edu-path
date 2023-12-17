<template>
  <div class="login-container">
    <div class="app-title">
      <h1>EduPath</h1>
    </div>
    <div class="login-section">
      <div class="login-box">
        <h2>Student Login</h2>
        <form @submit.prevent="loginUser">
          <div class="form-group">
            <input type="text" placeholder="Username" id="username" v-model="username" required>
          </div>
          <div class="form-group">
            <input type="password" placeholder="Password" id="password" v-model="password" required>
          </div>
          <button type="submit" class="login-btn">Login</button>
        </form>
      </div>
      <div class="signup-box">
        <h2>Not a student? Sign in here</h2>
        <button @click="redirectToAdminLogin" class="signup-btn">Sign in</button>
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
        username: '',
        password: '',
        errorMessage: ''
      };
    },
    methods: {
      async loginUser() {
        if (this.username === 'student' && this.password === 'password') {
          // Simulating a successful login
          console.log('Login successful');
          this.$router.push("/studentdashboard")
        }
        else {
          const response = await axios.post('login', {
            userid: this.username,
            password: this.password,
            role: "student"
          }).catch(err => { return err });
          this.errorMessage = response.data.message,
            this.password = ''
          if (this.errorMessage === "logged in succesfully") {
            this.$router.push("/studentdashboard")
          }
        }
      },
      redirectToAdminLogin() {
        this.$router.push({ name: 'AdminLogin' });
      }
    }
  };
</script>
<style scoped>
  .login-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    background-color: #f4f4f4;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }

  .app-title {
    margin-bottom: 50px;
    text-align: center;
  }

  h1 {
    font-size: 3rem;
    color: #333;
  }

  .login-section {
    display: flex;
    justify-content: space-around;
    width: 80%;
    max-width: 1200px;
  }

  .login-box,
  .signup-box {
    background-color: #fff;
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    width: 45%;
    max-width: 500px;
  }

  .login-box h2,
  .signup-box h2 {
    font-size: 2rem;
    margin-bottom: 30px;
    color: #333;
  }

  .form-group {
    margin-bottom: 20px;
  }

  label {
    font-weight: bold;
    display: block;
    margin-bottom: 5px;
  }

  input[type='text'],
  input[type='password'] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }

  .login-btn,
  .signup-btn {
    padding: 12px 25px;
    border: none;
    border-radius: 5px;
    background-color: #007bff;
    color: #fff;
    cursor: pointer;
    transition: background-color 0.3s ease;
    display: block;
    width: 100%;
    font-size: 1.2rem;
    text-align: center;
  }

  .login-btn:hover,
  .signup-btn:hover {
    background-color: #0056b3;
  }

  .error-message {
    color: red;
    margin-top: 20px;
    text-align: center;
  }
</style>