import Vue from 'vue'
import Vuex from 'vuex'
import jwtDecode from 'jwt-decode'

Vue.use(Vuex)

export default new Vuex.Store({
  // 상태 -> component의 data부분
  state: {
    token: null,  // token은 없다
  },
  // computed와 동일
  getters: {
    isLoggedIn(state) {
      return state.token ? true : false
    },
    options(state) {
      return {
        headers: {
          Authorization: 'JWT ' + state.token
        }
      }
    },
    userId(state) {
      return state.token ? jwtDecode(state.token).user_id : null
      // token값이 있다면 앞에꺼, 없다면 뒤에 null
    }
  },
  // 상태를 변경하는 함수
  mutations: {
    setToken(state, token) {
      state.token = token
    }
  },
  // methods 우리가 필요한 함수 로직들이 들어감으로써 변경할 수 있음
  actions: {
    login(context, token) {
      context.commit('setToken', token)
    },
    logout(context) {
      context.commit('setToken', null)
    }
  },
})
