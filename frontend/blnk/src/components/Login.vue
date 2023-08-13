<template>
    <v-container>
      <v-form>
        <v-text-field
          v-model="username"
          label="Username"
          required
        ></v-text-field>
        <v-text-field
          v-model="password"
          label="Password"
          required
          type="password"
        ></v-text-field>
        <v-btn
          color="primary"
          @click="login"
        >
          Login
        </v-btn>
      </v-form>
    </v-container>
  </template>

  <script>
  export default {
    name: "Login",
    data() {
      return {
        username: "",
        password: "",
      };
    },
    methods: {
      login() {
        axios
          .post("http://localhost:8000/api/users/login", {
            username: this.username,
            password: this.password,
          })
          .then((response) => {
            // If the login is successful, redirect the user to the home page
            if (response.status === 200) {
              window.location.href = "/";
            }
          })
          .catch((error) => {
            console.log(error);
            alert("Login failed");
          });
      },
    },
  };
  </script>
