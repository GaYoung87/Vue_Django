# Vuex (Vue + Django)

- **vue라우터: url별로 어떤 component를 보여줄지 렌더링 해주는 것**

- Django에서만 사용할 때
  - session-id 계속 제공 -> 한사람이 한개 이상 아이디도 가능 / server에 부담.

- vuex에서 사용하면  JSON 기반의 token주고받음
  - 유저확인까지 동일.
  - Client는 기존에 session id값을 받았지만, 이제는 Json Web Token을 받음
  - 보안은 조금 약함 but 빼앗기기 쉽지않고, JWT는 기한이 짧다.
  - 정보를 안전하게 JSON객체로 전송하기 위한 간결하고 독립적인 방법
  - 인증관련 로직을 서버와 클라이언트가 주고받을 때만 사용됨

- JWT
  - ex: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

- url별로 어떤 component를 사용할지



### Vue_Django 시작

```bash
student@M702 MINGW64 ~/development/Vue_Django
$ mkdir todo-back

student@M702 MINGW64 ~/development/Vue_Django/todo-back
$ python -V

$ venv

$ python -m venv venv   # (3.7.4)

$ source venv/Scripts/activate  # 가상환경 설정

$ pip list

$ python -m pip install --upgrade pip

$ pip install django

$ django-admin startproject todoback .

$ deactivate  # 가상환경에서 나옴

student@M702 MINGW64 ~/development/Vue_Django
$ vue create todo-front  # todo-back, todo-front 두개 만듦

student@M702 MINGW64 ~/development/Vue_Django/todo-front (master)
$ rm -rf .git  # todo-front는 git으로 관리되지 않음

student@M702 MINGW64 ~/development/Vue_Django/todo-front
$ rm .gitignore

student@M702 MINGW64 ~/development/Vue_Django
$ touch .gitignore   # gitignore파일 만들기
```

![image-20191118123547085](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191118123547085.png)

### vue에 router 설치

```bash
student@M702 MINGW64 ~/development/Vue_Django/todo-front (master)
$ vue ui  # Vue 프로젝트 매니저 실행
# 가져오기 - 플러그인 - router입력 후 설치 - history mode on -> 설치완료
# django처럼 여러페이지를 보여주는 것이아니라 하나의 페이지에서 변화가 생김
# Single Page Application: 요청과응답으로 페이지구성이 아니라, 그냥 화면만 바뀜 -> 어디로 갔는지 알기어려움
# history mode -> 어디로 갔는지 등등 알려줌

# 설치 후에 화면꺼줘야함
```

### router - index.js   :   url별로 어떤 component를 보여줄지 렌더링 해주는 것

```js
// router/index.js 파일에서 routes부분만 잘 보면 ok
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  // 하나의 큰 페이지 단위의 component -> views 안에 있는 component
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
```

- components: 페이지에서 사용되는 것들
- views: 하나의 큰 페이지 단위의 component

#### App.vue

```vue
<router-link to="/">Home</router-link> |
<router-link to="/about">About</router-link>
```

![image-20191118143419599](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191118143419599.png)

```vue
<template>
  <div id="app">
    <div id="nav">
        <!-- 화면에 보이게 함. -->
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view/>
  </div>
</template>

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
```



### Bootstrap 사용하기

```bash
student@M702 MINGW64 ~/development/Vue_Django/todo-front (master)
$ npm i bootstrap-vue bootstrap  # 꼭 todo-front에서 하기!
```



### Login.vue

```vue
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
```



### axios 설치

```bash
student@M702 MINGW64 ~/development/Vue_Django/todo-front (master)
$ npm i axios  # 꼭 todo-front에서 하기!
```



### LoginForm.vue 설치

```vue

```

### .env.local

- 디버그모드, api_key와 같은 것 적어놓는 파일

- 

- ![image-20191118162916322](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191118162916322.png)

  

### vue, django 둘다 동시에 키기

![image-20191118163949564](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191118163949564.png)