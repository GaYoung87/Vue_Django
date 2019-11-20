<template>
  <div class="todo-list">
    <div class="card mb-1" v-for="todo in todos" :key="todo.id">
      <div class="card-body d-flex justify-content-between">
        <span>{{ todo.title }}</span>
        <span @click="deleteTodo(todo)">delete</span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TodoList',
  // home에서 todolist 렌더링하고(호출해와서) 여기서 불러와서 보여주겠다.
  props: {
    todos: {
      type: Array,
      required: true,
    }
  },
  computed: {
    options() {
      return this.$store.getters.options
    }
  },
  methods: {
    deleteTodo(todo) {
      this.$session.start()
      // options만들어주려고 token만든 것이므로 options가 필요없어서 token도 지워야함
      // const token = this.$session.get('jwt')
      // const options = {
      //   headers: {
      //     Authorization: 'JWT ' + token
      //   }
      // }

      const SERVER_IP = process.env.VUE_APP_SERVER_IP

      axios.delete(`${SERVER_IP}/api/v1/todos/${todo.id}/`, this.options)  // 여기서 options를 넘겨줘야 token이 넘겨져서 가능해진다.
        .then(response => {
          console.log(response)
          const idx = this.todos.indexOf(todo)
          if (idx > -1) {
            this.todos.splice(idx, 1)  // 배열을 자르겠다
          }
        })
        .catch(error => {
          console.error(error)
        })

    },
  }
}
</script>

<style>

</style>