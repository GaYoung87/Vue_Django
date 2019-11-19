<template>
  <div class="todo-list">
    <div class="card mb-1" v-for="todo in todos" :key="todo.id">
      <div class="card-body d-flex justify-content-between">
        <span>{{ todo.title }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TodoList',
  // home에서 todolist 렌더링하고(호출해와서) 여기서 불러와서 보여주겠다.
  props: {
    todos: {
      type: Array,
      required: true,
    }
  }
}
</script>

<style>

</style>