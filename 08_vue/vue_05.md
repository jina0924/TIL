# Vue

[toc]

## Vue router

components

- 부품으로 쓰이는 애들

views

- url과 매핑되는 애들



Project setup

```bash
$ npm install
```

- pip install -r requirements.txt



폴더 구조

> 자유롭게 폴더구조 추가 가능

- api/

  - 새로 추가한 폴더

  - drf.js

    - 포스트맨에서 직접 작성하던 내용을 파일화 함

    ```js
    const HOST = 'http://localhost:8000/api/v1/'
    
    const ACCOUNTS = 'accounts/'
    
    export default {
      accounts: {
        login: () => HOST + ACCOUNTS + 'login/',
        ...
        // Token 으로 현재 user 판단
        currentUserInfo: () => HOST + ACCOUNTS + 'user/',
        // username으로 프로필 제공
        profile: username => HOST + ACCOUNTS + 'profile/' + username,
      },
    }
    ```

    - `drf.accounts.login()` : `http://localhost:8000/api/v1/accounts/login/` 을 리턴함

- components

  - 부품

- views

  - url과 매핑되는 애들 → 라우터에서 불러다 씀

- router

  - index.js

  - 기본 구조

    ```js
    const routes = [
        {
            path: '',
            name: '',
            component: '',	// 여기에 views의 파일들 불러다 씀 ex) LoginView
        },
    ```

    - path랑 name은 굳이 같지 않아도 됨



### 404 page

404 시나리오

1. Vue Router에 등록되지 않은 routes일 경우

   - vue router는 routes 배열에서 순차적으로 UPL을 검색

   ```js
   // router/index.js
   
     {
       path: '/404',
       name: 'NotFound404',
       component: NotFound404,
     },
     {
       path: '*',
       redirect: '/404',
     },  // 위치 중요함(위의 주소들을 제외한 모든 곳을 의미함. 마지막에 위치할 것)

2. Vue Router에는 등록되어 있지만, 서버에서 해당 리소스를 찾을 수 없는 경우

   - axios에서 catch로 넘어감





### Navigation Guard

전역 가드(Global Before Guards)

1. URL을 이동할 때마다, 이동하기 전 모든 경우에 발생

2. router 객체의 메서드

   - 콜백 함수를 인자로 받음
   - 해당 콜백 함수는 3개의 인자를 받음
     1. to: 이동하려는 route의 정보를 담은 객체
     2. from: 직전 route의 정보를 담은 객체
     3. next: 실제 route의 이동을 조작하는 함수

3. 반드시 마지막에 `next()`로 route이동을 실행해야 함

   ```js
   // router/index.js
   
   router.beforeEach((to, from, next) => {
     ...
   })
   ```

   - ex) to === 'profile/'이면 로그인했는지 물어봄 -> 안했으면 로그인 페이지면 옮겨버림

   ```js
   // router/index.js
   
   router.beforeEach((to, from, next) => {
     // 로그인 여부 확인 (Veux 사용시)
     const { isLoggedIn } = store.getters
     
     // Auth가 필요한 router의 name
     const noAuthPages = ['login', 'signup']
     
     // 현재 이동하고자 하는 페이지가 Auth가 필요한가
     const isAuthRequired = !noAuthPages.includes(to.name)
   
     // Auth가 필요한데, 로그인 되어있지 않다면?
     if (isAuthRequired && !isLoggedIn) {
       alert('Require Login. Redirecting..')
       // 로그인 페이지로 이동
       next({ name: 'login' })
     } else {
       // 원래 이동하려던 곳으로 이동
       next()
     }
   
     if (!isAuthRequired && isLoggedIn) {
       next({ name: 'articles' })
     }
   })
   ```

   

## Vuex

### Vuex Module

- Vuex는 코드 구조를 제한하지 않음
- index.js에는 모듈을 합치는 코드 작성
- accounts, articles 모듈 나눔



폴더 구조

- store

  - index.js

    ```js
    // store/index.js
    import accounts from './modules/accounts'
    
    export default new Vuex.Store({
        modules: {
            accounts.
        }
    })
    ```

    - 위에 처럼 모듈 불러와서 사용함

  - modules/

    - accounts.js

      ```js
      // modules/accounts.js
      
      export default {
          state: {
              ...
          },
          getters: {
              ...
          }
          ...
      }
      ```

      

Module의 이름 공간

- 줄 수도 있어도 안쓸 수도 있음



### Vuex-Component 구성

- 기본 구조

  ```js
  import router from '@/router'
  import axios from 'axios'
  import drf from '@/api/drf'
  
  
  export default {
    state: {
      token: // 요청 보낼때마다 쓸 토큰 값
      currentUser: // 토큰 값을 기반으로 현재 사용자 정보
      profile: // 누구의 프로필을 볼 것인지(?)
      authError: 
    },
    getters: {
      isLoggedIn: state => !!state.token,	// state에 토큰값이 있냐 없냐를 판별(T/F)
      currentUser: state => state.currentUser,
      profile: state => state.profile,
      authError: state => state.authError,
      authHeader: state => ({ Authorization: `Token ${state.token}`})
    },
  
    mutations: {
      SET_TOKEN: (state, token) => state.token = token,
      SET_CURRENT_USER: (state, user) => state.currentUser = user,
      SET_PROFILE: (state, profile) => state.profile = profile,
      SET_AUTH_ERROR: (state, error) => state.authError = error
    },
  
  ```

  - state랑 mutations은 개수 거의 동일함
    - SET_ 붙여서 함수 완성
  - state기반으로 추출할 수 있는 것들 -> getters
  - 모든 state는 getters를 통해서 접근함



### accounts Login

- signup과 구성 거의 같음
- data에 credential만들고 v-model로 묶어줌
- modules/accounts.js



### accounts Logout & Profile

logout

- 토큰 삭제

- accounts.js

  ```js
  axios({
      url: drf.accounts.logout(),
      method: 'post'
      headers: getters.authHeader,
    })
    .then() => {		// 보통 res인자 넘기는데 밑에서 안쓰니까 그냥 안받아도 됨(?)
      dispatch('removeToken')
      alert('성공적으로 로그아웃')
      router.push({ name: 'login' })
    })
    .error(err => {
      console.error(err.response)
    })
  ```

  - 로그아웃을 url에 적음 === 새로고침 => 새로고침하면 토큰값 변경될 수 있음 

  - ↓ 해결 방안

    ```js
    // accounts.js
    
      state: {
        token: localStorage.getItem('token') || '' ,
        currentUser: {},
        profile: {},
        authError: null,
      },

- LogoutView

  ```vue
  // router/LogoutView.vue
  
  <script>
  import { mapActions, mapGetters } from 'vuex'
  ...
  methods: {
    ...mapActions(['logout'])
  },
  computed: {
      ...mapGetters(['isLoggedIn'])
  }
  created() {
      if (this.isLoggedIn) {
          this.logout()
      } else {
          alert('잘못된 접근')
          this.$router.back()
      }
  }	// 해당 url로 넘어오자마자 로그아웃 해버림
  </script>
  ```

  로컬 스토리지에 토큰이 있으면 `token: localStorage.getItem('token') || '',`



### profile

- ProFileView.vue

  ```vue
  <template>
    ...
  </template>
  
  <script>
  import { mapGetters, mapActions } from 'vuex'
  
  export default {
    name: 'ProfileView',
    computed: {
      ...mapGetters(['profile'])
    },
    methods: {
      ...mapActions(['fetchProfile'])
    },
    created() {
      const payload = { username: this.$route.params.username }
      this.fetchProfile(payload)
    },
  }
  </script>
  ```

  - payload : 변수 처리된 username 넘김
  - `fetchProfile(payload)`로 username 넘김

  ```js
      fetchProfile({ commit, getters }, { username }) {
        /*
        GET: profile URL로 요청보내기
          성공하면
            state.profile에 저장
        */
        axios({
          url: drf.accounts.profile(username),
          method: 'get',
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_PROFILE', res.data)
          })
      },
  ```

  

### accounts Signup

- accounts.js

  ```js
  // store/modules/accounts.js
  import router from '@/router'
  import axios from 'axios'
  import drf from '@/api/drf'
  
  
  export default {
    // namespaced: true,
  
    // state는 직접 접근하지 않음
    state: {
      token: '',  // 로그인했을 때 받는 토큰 값
      currentUser: {},  // 토근 값을 기반으로 현재 사용자의 정보
      profile: {},  // 누구의 프로필을 볼 건지
      authError: null,
    },
    // 모든 state는 getters를 통해서 접근하겠다.(왜? 불러서 쓸 때 state따로 안부르고 getter로 부르기 위해)
    getters: {
      isLoggedIn: state => !!state.token, // 토큰값 유무에 따라 T/F로 나타나짐
      currentUser: state => state.currentUser,
      profile: state => state.profile,
      authError: state => state.authError,
      authHeader: state => ({ Authorization: `Token ${state.token}`})	// 함수가 아닌 객체를 반환한다는 의미로 소괄호로 한번 더 감쌈
    },
  
    mutations: {
      SET_TOKEN: (state, token) => state.token = token,
      SET_CURRENT_USER: (state, user) => state.currentUser = user,
      SET_PROFILE: (state, profile) => state.profile = profile,
      SET_AUTH_ERROR: (state, error) => state.authError = error,
    },
  
    actions: {
      saveToken({ commit }, token) {
        /* 
        state.token 추가 
        localStorage에 token 추가
        */
        commit('SET_TOKEN', token)
        localStorage.setItem('token', token)
      },
  
      removeToken({ commit }) {
        /* 
        state.token 삭제
        localStorage에 token 추가
        */
        commit('SET_TOKEN', '')
        localStorage.setItem('token', '')
      },
        
      signup({ commit, dispatch }, credentials) {
        /* 
        POST: 사용자 입력정보를 signup URL로 보내기
          성공하면
            응답 토큰 저장
            현재 사용자 정보 받기
            메인 페이지(ArticleListView)로 이동
          실패하면
            에러 메시지 표시
        */
        axios({
          url: drf.accounts.signup(),
          method: 'post',
          data: credentials	// 인자로 넘겨받은 credential이 통째로 data
        })
          .then(res => {
            const token = res.data.key	// res.data === json
            dispatch('saveToken', token)
            dispatch('fetchCurrentUser')
            router.push({ name: 'articles' })	// signup끝나면 메인 페이지로 이동
          })
          .catch(err => {
            console.error(err.response.data)
            commit('SET_AUTH_ERROR', err.response.data)
          })
      },
  ```

- fetchCurrentUser

  - 현재 사용자 정보를 기반으로 currentUser 채워줌
  - user정보 받아서 채워주는 용도
  - getters에 authHeader 만들어서 토큰값 넣을 수 있도록 함(매번 headers에 토큰값 채우지 않도록)
  - headers: getters.authHeader
  - 성공하면 mutations의 SET_CURRENT_USER 실행
  - 실패하면(유효하지 않은 토큰으로 시도한다면? )
    - if (err.response.status === 401)
      - dispatch('removeToken')
      - router.push({ name: 'login' })

- signup에서 토큰 저장하고 dispatch(fetchCurrentUser) 할 것



- SignupView

  ```vue
  // views.SignupView
  <template>
    <div>
      <h1>Signup</h1>
  
      <account-error-list v-if="authError"></account-error-list>
  
      <form @submit.prevent="signup(credentials)">
        <div>
          <label for="username">Username: </label>
          <input  v-model="credentials.username" type="text" id="username" required/>
        </div>
        <div>
          <label for="password1">Password: </label>
          <input v-model="credentials.password1" type="password" id="password1" required />
        </div>
        <div>
          <label for="password2">Password Confirmation:</label>
          <input v-model="credentials.password2" type="password" id="password2" required />
        </div>
        <div>
          <button>Signup</button>
        </div>
      </form>
    </div>
  </template>
  
  
  <script>
    import { mapActions, mapGetters } from 'vuex'
    import { mapActions, mapGetters } from 'vuex'
    import AccountErrorList from '@/components/AccountErrorList.vue'
  
    export default {
      data() {
        return {
          credentials: {
            username: '',
            password1: '',
            password2: '',
          }
        }
      },
      computed: {
        ...mapGetters(['authError'])
      },
      methods: {
        ...mapActions(['signup'])
      },
    }
  </script>
  ```

  - v-model을 credentials.username으로 하면 자동으로 묶임(객체 안의 키와 엮을 수 있음)



signup error

- err.res.data 안에 에러메시지 들어옴

- accounts.js

  - authError

- components/AccountErrorList.vue를 signup 실패시 보여줄 것

  - AccountErrorList.vue

    ```vue
    <template>
      <div class="account-error-list">
        <p v-for="(errors, field) in authError" :key="field">
          {{ field }}
          <ul>
            <li v-for="(error, idx) in errors" :key="idx">
              {{ error }}
            </li>
          </ul>
        </p>
    
      </div>
    </template>
    
    <script>
      import { mapGetters } from 'vuex'
      
      export default {
        name: 'AccountErrorList',
        computed: {
          ...mapGetters(['authError'])
        },
      }
    </script>
    
    <style>
      .account-error-list {
        color: red;
      }
    </style>
    ```

    



### articles Read / Like

- articles.js

  ```js
  getters: {
      articles: state => state.articles,
      article: state => state.article,
      isAuthor: (state, getters) => {
          return state.article.user.username === getters.currentUser.username
      },
      isArticle: () => {}	// state의 article이 비었는지 아닌지 확인하는 용
  },
  
  mutations: {
      SET_ARTICLES: (state, articles) => state.articles = articles,
      SET_ARTICLE: (state, article) => state.article = article,
  },
  actions : {
      fetchArticles({ commit, getters }) {
          axios({
              url: drf.articles.articles(),
              method:  'get',
              headers: getters.authHeader,
          })
          .then(res => commit('SET_ARTICLES', res.data))
           .catch(err => console.error(err.response)) // err만 쓰면 간단한 에러미시지
      }
  }
  ```

  - namespaced: true를 한다면 getters에 접근할 때 어디 getters인지 명시해줘야 함
    - 그게 아니라면 index.js에 합쳐진 getters가 됨

- ArticleListView

  ```vue
  <template>
  	<li v-for="article in articles" :key="article.pk">
          {{ article.user.username }} :
          <router-link :to="{ name: 'article', params: {articlePk: article.pk} }">				{{ article.title }}
      	</router-link>
        	({{ article.comment_count }}) | +{{ article.like_count }}
      </li>
  </template>
  
  <script>
  ...
  name: 'ArticleList',
  computed: {
      ...mapGetters(['articles'])
  },
  methods: {
      ...mapActions(['fetchArticles'])
  },
  create() {
      this.fetchArticles()
  }
  </script>
  ```



- ArticleDetailView.vue

  ```vue
  <script>
      computed: {
          ...mapGetters(['isAuthor', 'article'])
      }
  	methods: {
          ...mapActions(['fetchArticle'])
      }
  </script>
  ```

- articles.js

  - url에서 pk값 잡음
  - created()에서 담아서 보냄

- ArticleDetailView.vue

  ```vue
  <script>
  ...
  create() {
      const articlePk = this.$route.params.articlePk
  	this.fetchArticle(articlePk)
  }
  </script>
  ```

  - articlePk 재활용 하기 ↓

  ```vue
  <script>
    import { mapGetters, mapActions } from 'vuex'
    import CommentList from '@/components/CommentList.vue'
  
    export default {
      ...
      data() {
        return {
          articlePk: this.$route.params.articlePk,
        }
      },
      ...
      created() {
        this.fetchArticle(this.articlePk)
      },
    }
  </script>
  ```

  

- articles.js

  ```js
  fetchArticle({ commit, getters }, articlePk) {
      axios({
          url: drf.articles.article(articlePk),
          ...
      })
      .then(res => commit('SET_ARTICLE', res.data))
      .catch(err => {
          console.error(err.response)
          if (err.response.state === 404) {
              router.push({ name: 'NotFound404'})
          }
      })
  }
  ```



like

- articles.js

  ```js
  likeArticle({ commit, getters }) {
      axios({
          url: drf.articles.likeArticle()
          method: 'post',
          headers: getters.authHeader,
      })
  },
  ```

  

### articles C U D

- views

  - ArticleNewView.vue

  ```vue
  <template>
    <div>
      <h1>New Article</h1>
      <article-form :article="article" action="create"></article-form>
    </div>
  </template>
  
  <script>
    import ArticleForm from '@/components/ArticleForm.vue'
    export default {
      name: 'AritcleNewView',
      components: { ArticleForm },
      data() {
        return {
          article: {
            pk: null,
            title: '',
            content: '',
          }
        }
      },
    }
  </script>
  ```

- components

  - ArticleForm.vue

    - new랑 edit에서 재활용할 예정
    - new에서도 쓰기 위해서 빈 값을 인자로 넘김

    ```vue
    <script>
    import { mapActions } from 'vuex'
    
      export default {
        ...
        data() {
          return {
            newArticle: {
              title: this.article.title,
              content: this.article.content,
            }
          }
        },
        ...
    </script>
    ```

    - new에선 title, content가 빈 값
    - edit에선 title, content가 원래 있던 값으로 채워져 있음

    ```vue
    // ArticleForm.vue
    
    <script>
    import { mapActions } from 'vuex'
    
      export default {
        ...
        methods: {
          ...mapActions(['createArticle', 'updateArticle']),
          onSubmit() {
            if (this.action === 'create') {
              this.createArticle(this.newArticle)
            } else if (this.action === 'update') {
              const payload = {
                pk: this.article.pk,
                ...this.newArticle,
              }
              this.updateArticle(payload)
            }
          },
        },
      }
    </script>
    ```

    - 바로 createArticle안하고 onSumbit으로 건 이유
      - create와 update 구분하기 위해

- views.py

  - ArticleEditView.vue

    ```vue
    <template>
      <div>
        <h1>Edit Article</h1>
        <article-form v-if="isArticle" :article="article" action="update">
    
        </article-form>
      </div>
    
    </template>
    
    <script>
    import ArticleForm from '@/components/ArticleForm.vue'
    import { mapGetters, mapActions } from 'vuex'
      export default {
        name: 'AritcleEditView',
        components: { ArticleForm },
        computed: {
          ...mapGetters(['article', 'isArticle',])
        },
        methods: {
          ...mapActions(['fetchArticle'])
        },
        created() {
          this.fetchArticle(this.$route.params.articlePk)
        },
      }
    </script>
    ```

    - `'articles/<pk>/edit'`과 같은 주소이므로 fetchArticle에 `<pk>`값 넘겨야 함
    - form이 action이라는 props를 통해서 new인지 edit인지 구분하게 됨(?)
    - v-if 쓰는 이유
      - 비동기 작업이기 때문
      - 렌더링 하는 시간보다 Article이 늦게 도착하면 article 내용 안보임
      - article이 오기 전까지 렌더링 막아야 함

    ```js
    // modules/articles.js
    import _ from 'lodash'
    
    ...
      getters: {
        ...
        isArticle: state => !_.isEmpty(state.article),
      },
    ```

    - lodash 쓰는 이유
      - javascript에서는 빈 객체도 true이기 때문
      - lodash를 써서 빈 객체일 때 false로 판단하고 행동하도록 만듦

- modules/articles.js

  ```js
      updateArticle({ commit, getters }, { pk, title, content}) {
        axios({
          url: drf.articles.article(pk),	// url : drf.articles.artice(article.pk)
          method: 'put',
          data: { title, content }, 	// data: { title: article.title, ...}
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_ARTICLE', res.data)
            router.push({
              name: 'article',
              params: { articlePk: getters.article.pk }
            })
          })
      },
  ```

  - `{ pk, title, content}`로 한 이유 => 인자를 하나만 받고 나머지는 버리기 때문
  - `updateArticle({ commit, getters }, article)` →   `updateArticle({ commit, getters }, { pk, title, content})` 변경 이유
    - 밑에서 url, data에서 article.pk, article.title 와 같이 반복해서 쓰는 경우를 줄이기 위해

  

- state가 비어있을 때 state.article.user.username을 찍으면 아무것도 없어서 console창에서 에러남

  → state.article.user?.username

  - user 있으면 username, 없으면 undefined



### Comments C R D







### Comments Update





## Navigation guard

로그인이 안되어 있을 때 접근 막는법

- 애플리케이션 전역에서 동작하는 전역 가드
- 특정 url에서만 동작하는 라우터 가드
- 컴포넌트 가드(많이 쓰지 X)

cd

vue add router

npm run serve

npm i axios



모듈은 프로젝트에서 크게 신경쓰지 않아도 됨