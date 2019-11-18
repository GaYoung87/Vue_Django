<template>
  <div class="login-div">

    <div v-if="loading" class="spinner-border" role="status">
      <span class="sr-only">loading..</span>
    </div>

    <div class="login-form">

      <div v-if="errors.length" class="alert alert-danger">
        <h4>다음의 오류를 해결해주세요.</h4>
        <hr>
        <div v-for="(error, idx) in errors" v-bind:key="idx">{{ error }}</div>
      </div>

      <div class="form-group">
        <!-- 위의 label은 아래의 input값을 가진다 -->
        <label for="id">ID</label>
        <input type="text" id="id" class="form-control" placeholder="아이디를 입력해주세요" v-model="credentials.username">
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" id="password" class="form-control" placeholder="비밀번호를 입력해주세요" v-model="credentials.password">  <!-- 위의 label은 아래의 input값을 가진다 -->
      </div>
      <div>
        <button class="btn btn-success" v-on:click="login">Login</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LoginForm',
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      },
      loading: false,
      errors: [],
    }
  },
  methods: {
    login() {
      if(this.checkForm()) {  // 함수가 유효한지 아닌지 알려줌
        this.loading = true  // 로그인 요청 시작하면 true
        const SERVER_IP = process.env.VUE_APP_SERVER_IP


        axios.get(SERVER_IP, this.credentials)
          .then(response => {
            console.log(response)
            this.loading = false  // 로그인 요청 끝나면 false
          })
          .catch(error => {
            console.error(error)
            this.loading = false  // 로그인 요청 끝나면 false
          })
      }
    },
    checkForm() {
      this.errors = []  // 매번 검사할 때마다 초기화
      if (!this.credentials.username) {
        this.errors.push('아이디를 입력해주세요')
      }
      if (this.credentials.password.length < 8) {
        this.errors.push('비밀번호는 8글자 이상 입력해주세요')
      }
      if (this.errors.length === 0) {
        return true
      }  // true가 아니라면 return undefined (falsy)이므로 굳이 작성하지 않아도 ok
    },
  },
}
</script>

<style>

</style>