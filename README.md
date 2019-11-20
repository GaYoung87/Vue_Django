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

1. **settings**

```python
"""
Django settings for todoback project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2t2%$p1f$oqwf_8pn8zfc8-qr%325p4p)kpu@!5k!^!arim426'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # local apps
    'todos',

    # Third party apps
    'rest_framework',
    'corsheaders',

    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# jwt 관련 세팅
# http://jpadilla.github.io/django-rest-framework-jwt/#usage
REST_FRAMEWORK = {
    # 로그인 여부를 확인해주는 클래스
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    # 인증여부를 확인해주는 클래스
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

# http://jpadilla.github.io/django-rest-framework-jwt/#additonal-settings
JWT_AUTH = {
    # Token을 서명할 시크릿 키를 등록(절대 외부 노출 금지!) default가 settings.py에 있는 SECRET_KEY이긴 하다.
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
    'JWT_ALLOW_REFRESH': True,  # Token은 유효기간 끝날때까지 사용 가능 -> 유효기간 짧지만, 자주 최신화해서 새로운 token을 발행시킨다.
    # 개발시에는 token을 1주일 유효하게 설정(자꾸 로그인하면 힘듦), default 유효기간은 5분
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    # 28일 마다 token이 갱신(유효기간 연장시)
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=28),
    # token = access token: 받은 access token으로 우리에게 정보 요청
    # refresh token: 사용자가 이걸 보내면 우리는 다시 access token을 준다
}

MIDDLEWARE = [
    # https://github.com/adamchainz/django-cors-headers/#setup
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# https://github.com/adamchainz/django-cors-headers#cors_origin_whitelist
CORS_ORIGIN_WHITELIST = [
    "http://localhost:8080",
]

# open_api라면 전세계 모든 곳에서 접근 가능!
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'todoback.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'todoback.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# customising한 후에는 등록해줘야 사용가능. -> 앞으로 todos에 정의한 User모델을 기본 user모델로 사용
AUTH_USER_MODEL = 'todos.User'
```

2. **models.py**

   ```python
   from django.db import models
   from django.conf import settings
   from django.contrib.auth.models import AbstractUser
   
   # 안에 내용을 추가하지 않고 명시적으로 만들어서 사용하겠다.
   # 유저는 customising된 유저를 사용(default 유저를 사용하더라도 장고에서는 *강력히* 커스텀 유저를 사용하라고 권장)
   class User(AbstractUser):
       pass
   
   class Todo(models.Model):
       user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
       title = models.CharField(max_length=50)
       completed = models.BooleanField(default=False)
   
       # Todo 사용할때마다 terminal에 찍히게 해서 내가 확인하려고 작성
       def __str__(self):
           return self.title
   ```

3. **urls.py**

```python
"""todoback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# http://jpadilla.github.io/django-rest-framework-jwt/#usage
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    # 일치한다면 보여주는 token
    path('api-token-auth/', obtain_jwt_token),
]
```

4. token값 받기![image-20191119112035495](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191119112035495.png)

5. 오른쪽의 token을 어디에 저장할 것인가?

   ```vue
   // LoginForm.vue에서 login부분 수정
     methods: {
       login() {
         if(this.checkForm()) {  // 함수가 유효한지 아닌지 알려줌
           this.loading = true  // 로그인 요청 시작하면 true
           // http://127.0.0.1:8000
           const SERVER_IP = process.env.VUE_APP_SERVER_IP
   
   
           axios.post(SERVER_IP + '/api-token-auth/', this.credentials)
             .then(response => {
   
               // 세션을 초기화, 사용하겠다!
               this.$session.start()
   
               // 응답 결과를 세션에 저장하겠다!(key, value값을 받음 -> 이 key값에 value를 저장하겠다)
               this.$session.set('jwt', response.data.token)
   
               this.loading = false  // 로그인 요청 끝나면 false
             })
             .catch(error => {
               console.error(error)
               this.loading = false  // 로그인 요청 끝나면 false
             })
         }
   ```

   

6. ![image-20191119113052252](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191119113052252.png)



## Vue

```bash
student@M702 MINGW64 ~/development/Vue_Django/todo-front (master)
$ npm install vue-session
```

### todo-front의 main.js

```js
// todo-front의 main.js
import Vue from 'vue'
import App from './App.vue'
import router from './router'
// 만약 폴더만 지정해놓고 어떤 파일인지 등록하지 않았으면 폴더 안의 index.js파일을 찾아감
import BootstrapVue from 'bootstrap-vue'
import VueSession from 'vue-session'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
Vue.use(VueSession)  // 앞으로 Vue에서 Vuesession 사용할 수 있음
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
```

### todo-front의 LoginForm.vue

```vue
methods: {
    login() {
      if(this.checkForm()) {  // 함수가 유효한지 아닌지 알려줌
        this.loading = true  // 로그인 요청 시작하면 true
        // http://127.0.0.1:8000
        const SERVER_IP = process.env.VUE_APP_SERVER_IP


        axios.post(SERVER_IP + '/api-token-auth/', this.credentials)
          .then(response => {

            // 세션을 초기화, 사용하겠다!
            this.$session.start()

            // 응답 결과를 세션에 저장하겠다!(key, value값을 받음 -> 이 key값에 value를 저장하겠다)
            this.$session.set('jwt', response.data.token)

            this.loading = false  // 로그인 요청 끝나면 false
            router.push('/')  // home으로 보내준다
          })
          .catch(error => {
            console.error(error)
            this.loading = false  // 로그인 요청 끝나면 false
          })
      }
```

### Home.vue

```vue
<template>
  <div class="home">

  </div>
</template>

<script>
import router from '@/router'

export default {
  name: 'Home',

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
    }
  },
  // Vue가 화면에 그려지면 실행하는 함수
  mounted() {
    this.checkLoggedIn()
  }
}
</script>

<style>

</style>
```

### App.vue 

```vue
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
```



## Django

1. **serializers.py**

```python
from rest_framework import serializers
from .models import Todo

class TotoSerializer(serializers.ModelSerailizer):
    class Meta:
        model = Todo
        fields = ('id', 'user', 'title', 'completed',)
```

2. **urls.py(todoback)**

```python
from django.contrib import admin
from django.urls import path, include
# http://jpadilla.github.io/django-rest-framework-jwt/#usage
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    # 일치한다면 보여주는 token
    path('api-token-auth/', obtain_jwt_token),
    path('api/v1/', include('todos.urls')),
]
```

3. **create**
   - urls.py(todos)

```python
from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_create, name='todo_create'),
]
```

- views.py

```python
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo


@api_view(['POST'])  # 특정 method의 요청만 허용하겠다
def todo_create(request):
    # request.data는 axios의 body로 전달한 데이터
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        # 사용자가 새롭게 작성한 데이터를 응답해준다.
        return Response(serializer.data)
```

- 그리고 나서 postman에서 확인

![image-20191119141402736](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191119141402736.png)

![image-20191119141711782](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191119141711782.png)

- 이 토큰을 가지고 아까거기에 JWT+빈칸한칸+token붙이기![image-20191119142912347](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191119142912347.png)



4. **update_and_delete**
   - urls.py

```python
 path('todos/<int:todo_id>/', views.todo_update_delete),
```

- views.py

```python
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo

@api_view(['PUT', 'DELETE'])
def todo_update_delete(request, todo_id):
    # 수정하거나 삭제할 todo instance 호출
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'PUT':
        # instance todo를 request.data로 넘어온 값으로 수정하겠다.
        serializer = TodoSerializer(instance=todo, data=request.data)  # data=수정하겠다고 하는 data
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    if request.method == 'DELETE':
        todo.delete()
        return Response(status=204)
```

- 그리고 나서 postman에서 확인
- 수정확인![image-20191119144013895](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191119144013895.png)

- 삭제 확인

  ![image-20191119144159630](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191119144159630.png)

5. **user_detail**
   - urls.py

```python
path('users/<int:user_id>/', views.user_detail),
```

- views.py

```python
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer, UserDetailSerializer
from django.contrib.auth import get_user_model
from .models import Todo

User = get_user_model()

@api_view(['GET'])
def user_detail(request, user_id):
   user = get_object_or_404(User, pk=user_id)
   serializer = UserDetailSerializer(instance=user)
   return Response(serializer.data)
```

- 그리고 나서 postman에서 확인

![image-20191119151535105](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191119151535105.png)



## Vue

```bash
student@M702 MINGW64 ~/development/Vue_Django/todo-front (master)
$ npm i jwt-decode  # 우리가 가지고있는 token에서 필요한 정보를 빼가지고온다.
```

### 1. App.vue

```vue
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

```

### 2. Home.vue

```vue
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
```

### 3. TodoList.vue

```vue
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
  methods: {
    deleteTodo(todo) {
      this.$session.start()
      const token = this.$session.get('jwt')
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }

      const SERVER_IP = process.env.VUE_APP_SERVER_IP

      axios.delete(`${SERVER_IP}/api/v1/todos/${todo.id}/`, options)  // 여기서 options를 넘겨줘야 token이 넘겨져서 가능해진다.
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
```

### 4. TodoInput.vue

```vue
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
```

