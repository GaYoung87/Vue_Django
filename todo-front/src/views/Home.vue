<template>
  <div class="home">

  </div>
</template>

<script>
import router from '@/router'

export default {
  name: 'Home',

  methods: {
    // 사용자 로그인 유무를 확인하여 로그인 되어있지 않을 시 로그인 페이지로 보내겠다.
    checkLoggedIn() {
      // 1. 세션을 시작해서
      this.$session.start()

      // 2. 'jwt'가 있는지 확인하겠다.
      if(!this.$session.has('jwt')) {  // session에 jwt라는 값이 저장되어있는지 물어봄
        // jwt가 없다면 로그인 페이지로 보내겠다.
        router.push('/login')
      }
    }
  },
  // Vue가 화면에 그려지면 실행하는 함수
  mounted() {
    this.checkLoggedIn()
  }
}
</script>

<style>

</style>