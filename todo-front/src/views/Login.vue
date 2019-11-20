<template>
  <div>
    <h1>로그인 페이지 입니다.</h1>
    <!-- 3. Components 사용 -->
    <LoginForm />
  </div>
</template>

<script>
// 1. Components 호출한다.
import LoginForm from '@/components/LoginForm'
export default {
  name: 'Login',

  // 2. Components 등록
  components: {
    LoginForm,
  }
}
</script>

<style>

</style>