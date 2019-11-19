<template>
  <div class="home">
    <h1>Todo</h1>
    <TodoInput @createTodo="createTodo" />
    <TodoList :todos="todos"/>
    
  </div>
</template>

<script>
import axios from 'axios'
import jwtDecode from 'jwt-decode'
import TodoList from '@/components/TodoList'
import TodoInput from '@/components/TodoInput'
import router from '@/router'


export default {
  name: 'Home',

  data() {
    return {
      todos: [],
    }
  },

  // home에서 todolist 렌더링하고(호출해와서) 여기서 불러와서 보여주겠다.
  components: {
    TodoList,
    TodoInput,
  },

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
    },

    // 우리가 만든 django API서버로 todos를 달라는 요청을 보낸 뒤, todos data에 할당하는 함수
    getTodo() {
      
      this.$session.start()  // 무조건 1순위
      const token = this.$session.get('jwt')  // 이름 지어줌
      const userId = jwtDecode(token).user_id

      const SERVER_IP = process.env.VUE_APP_SERVER_IP

      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      axios.get(`${SERVER_IP}/api/v1/users/${userId}/`, options)  // http://127.0.0.1:8000/api/v1/users/1/에서 우리는 데이터를 본다.
        .then(response => {
          this.todos = response.data.todo_set
        })
        .catch(error => {
          console.log(error)
        })
    },
    createTodo(title) {
      this.$session.start()
      const token = this.$session.get('jwt')
      const userId = jwtDecode(token).user_id
      const SERVER_IP = process.env.VUE_APP_SERVER_IP

      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }

      const data = {
        title,
        user: userId
      }

      axios.post(`${SERVER_IP}/api/v1/todos/`, data, options)
        .then(response => {
          this.todos.push(response.data)
          // console.log(response.data)
        })
        .catch(error => {
          console.error(error)
        })
    },
  },
  // Vue가 화면에 그려지면 실행하는 함수
  mounted() {
    this.checkLoggedIn()
    this.getTodo()
  }
}
</script>

<style>

</style>