<template>
  <div class="todo-input">
    <!-- prevent: 실제 제출 행위를 막아서 요청이 발생하는 일이 없도록 함 -->
    <form class="input-group mb-3" @submit.prevent="onSubmit">
      <input v-model="title" type="text" class="form-control">
      <button type="submit" class="btn btn-success">add</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'TodoInput',
  data() {
    return {
      title: ''
    }
  },
  methods: {
    onSubmit() {
      // emit은 component가 이벤트를 발생시키게 하는 함수 -> createTodo라는 이벤트 발생시킴
      this.$emit('createTodo', this.title)
      this.title = ''
    }
  }
}
</script>

<style>

</style>