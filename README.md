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



### LoginForm.vue 

```vue
<template>
  <div class="login-div">

    <div v-if="loading" class="spinner-border" role="status">
      <span class="sr-only">loading..</span>
    </div>

    <div class="login-form">

      <div v-if="errors.length" class="alert alert-danger">
        <h4>다음의 오류를 해결해주세요.</h4>
        <hr>
        <div v-for="(error, idx) in errors" v-bind:key="idx">{{ error }}</div>
      </div>

      <div class="form-group">
        <!-- 위의 label은 아래의 input값을 가진다 -->
        <label for="id">ID</label>
        <input type="text" id="id" class="form-control" placeholder="아이디를 입력해주세요" v-model="credentials.username">
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" id="password" class="form-control" placeholder="비밀번호를 입력해주세요" v-model="credentials.password">  <!-- 위의 label은 아래의 input값을 가진다 -->
      </div>
      <div>
        <button class="btn btn-success" v-on:click="login">Login</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LoginForm',
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      },
      loading: false,
      errors: [],
    }
  },
  methods: {
    login() {
      if(this.checkForm()) {  // 함수가 유효한지 아닌지 알려줌
        this.loading = true  // 로그인 요청 시작하면 true
        const SERVER_IP = process.env.VUE_APP_SERVER_IP


        axios.get(SERVER_IP, this.credentials)
          .then(response => {
            console.log(response)
            this.loading = false  // 로그인 요청 끝나면 false
          })
          .catch(error => {
            console.error(error)
            this.loading = false  // 로그인 요청 끝나면 false
          })
      }
    },
    checkForm() {
      this.errors = []  // 매번 검사할 때마다 초기화
      if (!this.credentials.username) {
        this.errors.push('아이디를 입력해주세요')
      }
      if (this.credentials.password.length < 8) {
        this.errors.push('비밀번호는 8글자 이상 입력해주세요')
      }
      if (this.errors.length === 0) {
        return true
      }  // true가 아니라면 return undefined (falsy)이므로 굳이 작성하지 않아도 ok
    },
  },
}
</script>

<style>

</style>
```

### .env.local

- 디버그모드, api_key와 같은 것 적어놓는 파일

  ![image-20191118162916322](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191118162916322.png)

  


### vue, django 둘다 동시에 키기

![image-20191118163949564](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191118163949564.png)



## Django

- **CROS error**
- vue 화면을 키면 Access to XMLHttpRequest at 'http://127.0.0.1:8000/' from origin 'http://localhost:8080' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource. 이런 에러가 뜬다.
- vue방에서 django방으로 가는 것을 허용하지 않음
- 일단 django에 접속해서 자료를 빼내갈 이상한 애들이 있으므로,  일단 다 막고, vue를 화이트리스팅 처리를 한다.

```bash
# 1. django app 만들기
student@M702 MINGW64 ~/development/Vue_Django/todo-back (master)
$ python manage.py startapp todos

# 2. DRF 설치
$ pip install djangorestframework

# 3. 인증구현 가능한 jwt 설치
$ pip install djangorestframework-jwt

# 4. 
$ pip install django-cors-headers
```

- django rest framework jwt 관련 세팅 적용 -> settings.py에 작성 (다양한 설정)
- url에서 token 사용가능하게 추가 -> todoback의 urls.py에 작성



```python

```

