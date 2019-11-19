<template>
 <div id="app">
   <div id="nav">
     <!-- 컴포넌트가 화면에 보여주도록 하기 위해 router-link 를 해주었지만 logout은 화면에 보여주는게 아닌 하나의 기능이기 때문에 a-tag로 해도 상관없다. -->
     <!-- isLoggedIn 값에 따라서 조건부 렌더링 -->
     <div v-if="isLoggedIn">
       <router-link to="/">Home</router-link> |
       <!-- a-tag 는 새로고침을 해준다. 따라서 push(login)이 먹었다가 다시 logout으로 가게 된다. -->
     <!-- prevent 를 사용하는 이유는 href 로 redirect 를 방지하기 위함 -->
     <a @click.prevent="logout" herf="/logout">Logout</a>
     </div>
     <div v-else>
       <router-link to="/login">Login</router-link>
     </div>
   </div>
   <div class="container col-6">
     <router-view/>
   </div>
 </div>
</template>
<script>
import router from  '@/router'
export default {
 name: 'App',
 data() {
   return {
     isLoggedIn: this.$session.has('jwt')
   }
 },
 methods: {
     logout() {
         this.$session.destroy()
         router.push('/login')
     }
 },
 // data 에 변화가 일어나는 시점에 실행하는 함수
 updated() {
   this.isLoggedIn = this.$session.has('jwt')
 }
}
</script>
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