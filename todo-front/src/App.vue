<template>
  <div id="app">
    <div id="nav">
      <!-- isLoggedIn 값에 따라서 조건부 렌더링 -->
      <div v-if="isLoggedIn">
        <router-link to="/">Home</router-link> | 
        <!-- logout component 없음 -> logout은 하나의 기능일 뿐! -->
        <!-- 사용자가 어디로 이동했는지에 대한 기록을 남기기 위해 logout, 아니면 href="login"을 써도 ok -->
        <!-- 새로고침 하지 않아도 logout됨 -->
        <!-- prevent를 사용하는 이유는 href로 redirect를 방지하기 위해 -->
        <a @click.prevent="logout" href="/logout">Logout</a>
      </div>
      <div v-else>
        <!-- 로그인 페이지로 가게 링크를 달아줌 -->
        <router-link to="/login">Login</router-link>
      </div>  
      
    </div>
    <div class="container col-6">
      <router-view/>
    </div>
  </div>
</template>


<script>
import router from '@/router'
export default {
  name: 'App',


  // login이 되어있으면 home, logout 보이기

  data() {
    return {
      // 사용자의 로그인 상태 값, jwt가 있으면 true,
      isLoggedIn: this.$session.has('jwt')
    }

  },

  methods: {
    logout() {
      this.$session.destroy()  // 세션을 통째로 날려주겠다.
      router.push('/login')  // 날리고 나서는 로그인 페이지로 보내라
    }
  },

  // data에 번화가 일어나는 시점에 실행하는 함수
  updated() {
    this.isLoggedIn = this.$session.has('jwt')
  }
}
</script>>



<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
