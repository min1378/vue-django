<template>
  <div class="todo-list">
    <div class="card" v-for="todo in todos" :key="todo.id">
      <div class="card-body d-flex justify-content-between">
        <span> {{ todo.title }} </span>
        <span @click="deleteTodo(todo)">삭제</span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'




export default {
  name: "TodoList",
  props: {
    todos: {
      type: Array,
      required: true,
    }
  },
  methods: {
    deleteTodo(todo) {
      this.$session.start()
      const token = this.$session.get('jwt')
      const options = {
        headers:{
          Authorization: 'JWT ' + token
        }
      }
      const SERVER_IP = process.env.VUE_APP_SERVER_IP

      axios.delete(`${SERVER_IP}/api/v1/todos/${todo.id}/`, options)
        .then(response =>{
          console.log(response)
          const targetTodo = this.todos.find(item => {
            return item === todo
          })
          const idx = this.todos.indexOf(targetTodo)
          if (idx > -1) {
            this.todos.splice(idx, 1)
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