<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">
      <v-img height="300" src="@/assets/logo.svg" />


      <h1 class="text-h2 font-weight-bold">BLNK</h1>

      <div class="py-14" />

      <v-row class="d-flex align-center justify-center">
        <v-col cols="auto">
          <v-btn
            href="/login"
            min-width="164"
            rel="noopener noreferrer"
            variant="text"
          >
            <v-icon
              icon="mdi-view-dashboard"
              size="large"
              start
            />
            Login
          </v-btn>

        </v-col>

        <v-col cols="auto">
          <v-btn
            to="/register"
            min-width="164"
            rel="noopener noreferrer"
            variant="text"
          >
            <v-icon
              icon="mdi-account-group"
              size="large"
              start
            />

            Register
          </v-btn>

        </v-col>
      </v-row>
    </v-responsive>
  </v-container>
</template>

<script setup>
  //
</script>
