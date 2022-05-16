# Vuex

[toc]



## Vuex intro

### Vuex

- "Statement management pattern + Library:" for vue.js
- 상태를 전역 저장소로 관리할 수 있도록 지원하는 라이브러리
  - 상태가 예측 가능한 방식으로만 변경될 수 있도록
    - 예측 불가능한 경우: 자바스크립트 비동기
  - 중앙 집중식 저장소 역할
- Vue의 공식 devtools와 통합되어 기타 고급 기능을 제공



**State**

- state는 곧 data



**상태 관리 패턴**

- 컴포넌트의 공유된 상태를 추출하고 이를 전역에서 관리 하도록 함
- 컴포넌트는 커다란 view
- 모든 컴포넌트는 트리에 상관없이 상태에 액세서하거나 동작을 트리거 할 수 있음
- 코드의 구조와 유지 관리 기능 향상



**기존 Pass props & Emit event**

- 단방향 데이터 흐름
  - state는 앱을 작동하는 원본 소스(data)
  - view는 state의 선언적 매핑
  - action은 view에서 사용자 입력에 대해 반응적으로 state를 바꾸는 방법 (methods)



**Vuex management pattern**

- 중앙 저장소에 state를 모아놓고 관리
- 규모가 큰 (컴포넌트 중첩이 깊은)프로젝트에서 매우 효율적
- 각 컴포넌트에서는 중앙 집중 저장소의 state만 신경 쓰면 됨
  - 동일한 stats를 공유하는 다른 컴포넌트들도 동기화됨



**Vuex를 활용한 state(상태) 관리**

1. 상태 흐름 관리가 매우 중요해짐
2. 상태 변화는 오로지 Vuex가 관리
   - 상태의 변화는 모든 컴포넌트에서 공유
   - 상태의 변화는 오로지 Vuex가 관리 -> 해당 상태를 공유하고 있는 모든 컴포넌트는 변화에 반응함
3. A 컴포넌트와 같은 상태를 공유하는 다른 컴포넌트 신경 x -> 오로지 상태의 변화를 Vuex에 알림





## Vuex Core Concepts

**Vuex 핵심 컨셉**

![Vuex concepts image](vuex.assets/vuex.png)

1. **State**
   - 중앙에서 관리하는 모든 상태 정보(data)
     - 원본 소스(single source of truth)의 역할
     - 각 애플리케이션마다 하나의 저장소만 갖게 됨
   - 여러 컴포넌트 내부에 있는 특정 state를 중앙에서 관리하게 됨
   - State가 변화하면 해당 state를 공유하는 여러 컴포넌트의 DOM은 (알아서) 렌더링
2. **Mutations**
   - data의 변경
   - 실제로 state를 변경하는 유일한 방법
   - mutation의 handler(핸들러 함수)는 반드시 **동기적**이어야 함
     - 비동기적 로직은 state가 변화하는 시점이 의도한 것과 달라질 수 있음(추적할 수 없음)
     - Actions에서 commit() 메서드에 의해 호출됨
       - commit : v. 저지르다
   - 첫 번째 인자로 항상`state`를 받음
   - Actions에서 `commit()` 메서드에 의해 호출됨
3. **Actions**
   - 함수 = 모든 행동
   - Mutations와 유사하지만(둘 다 함수) 다음과 같은 차이점이 있음
     1.  state를 변경하는 대신 mutations를 commit() 메서드로 호출해서 실행
     2. 비동기 작업이 포함될 수 있음
   - `context` 객체 인자를 받음
     - state를 직접 변경하지 않음
   - 컴포넌트에서 `dispatch()` 메서드에 의해 호출됨
     - dispatch : v. 호출하다
   - Actions를 통해 state를 조작할 수 있지만, state는 오로지 Mutations를 통해 조작해야 함
     - 명확한 역할 분담을 위해
4. **Getters**
   - state를 변경하지 않고 활용하여 계산을 수행 (computed와 유사)
     - state를 특정한 조건에 따라 구분(계산)만 함
     - 계산된 값을 가져옴



## Vuex Todo App

### Set project & components

- vuex 추가

  ```bash
  $ vue add vuex
  ```



**index.js**

- 기본 파일, 대표 파일을 의미
- Vuex core concepts가 작성되는 곳
- template, script, style에서 script 역할 축소됨



M V VM

- M: data 객체
- V : DOM(HTML)
- VM : component 트리



### Create Todo

**[주의]**

- Vuex를 사용한다고 해서 Vuex Store에 모든 상태를 넣어야 하는 것은 아님
- 간단한 데이터들은 props & emit 사용하기도 함



**TodoList 데이터 가져오기**

- 컴포넌트에서 Vuex Store의 state에 접근
  - `$store.state`



**Computed로 변경**

- todo가 추가되는 등의 변경 사항이 있을 때만 새로 계산한 값을 반환하는 방향

- this로 접근

  ```vue
  <template>
    <div>
      <!-- <todo-list-item
      v-for="todo in $store.state.todos"
      :key="todo.date"> -->
      <todo-list-item
      v-for="todo in todos"
      :key="todo.date" 
      :todo="todo">
  
      </todo-list-item>
    </div>
  </template>
  
  <script>
  computed: {
  	todos () {  // : function 생략
  		return this.$store.state.todos
      }
  }
  </script>
  ```



**Actions & Mutations**

- createTodo 메서드를 통해 createTodo Action 함수 호출

  ```vue
  <script>
  ...
    methods: {
      createTodo() {
        this.$store.dispatch('createTodo', newTodo)
        this.todoTitle = ''
      }
    }
  ...
  </script>
  ```

- Actions

  - createTodo 함수
  - CREATE_TODO mutation 함수 호출

- Mutations

  - CREATE_TODO 함수
  - State의 todo 데이터 조작

  ```js
  export default new Vuex.Store({
      ...
    mutations: {    // change
      CREATE_TODO(state, newTodo) {   // mutation는 무조건 첫 번째 인자로 state 받음. 강조의 의미로 ALL CAPITAL
        state.todos.push(newTodo)
      },
    },
    actions: {    // methods
      createTodo(context, newTodo) {
        // context -> 맥가이버 칼
        // context.commit('CREATE_TODO')
        // const commit = context.commit
        // const { commit } = context
        console.log(newTodo)
        context.commit('CREATE_TODO', newTodo)
        // context.dispatch('saveTodos')
      },
  ```

  - Javascript Destructuring assignment (구조 분해 할당)

    - 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법
    - 변수명과 키 값이 같을 때 사용 가능
    
    ```js
    actions: {
        createTodo: function (context, todoItem) {
            context.commit('CREATE_TODO', todoItem)
        }
    }
    ```
    
    ↓ 변경 후
    
    ```js
    actions: {
        createTodo: function ({ commit }, todoItem) {
            commit('CREATE_TODO', todoItem)
        }
    }
    ```
    
    

**Actions의 "context" 객체**

- Vuex store의 전반적인 맥락 속성을 모두 포함하고 있음
- context.commit -> mutation 호출
- context.state -> state 접근
- context.getters -> getters 접근
  - dispatch()로 다른 actions도 호출 가능



### Delete Todo

- deleteTodo action 함수 호출

  ```vue
  <template>
    ...
        <button @click="deleteTodo(todo)">Delete</button>
      ...
  </template>
  
  <script>
  export default {
    ...
    props: {
      todo: Object,
    },
    methods: {
      deleteTodo: function () {
      this.$store.dispatch('deleteTodo', this.todo)
      },
    }
  }
  </script>
  ```

- Actions & Mutations

  ```js
    actions: {
      ...
      deleteTodo: function({ commit }, todoItem) {
        commit('DELETE_TODO', todoItem)
      },
    },
  ```

  ```js
    mutations: {
      ...
      DELETE_TODO: function (state, todoItem) {
        // 1. todoItem이 첫 번째로 만나는 요소의 index를 가져옴
        const index = state.todos.indexOf(todoItem)
  
        // 2. 해당 index 1개만 삭제하고 나머지 요소를 토대로 새로운 배열 생성
        this.state.todos.splice(index, 1)
      },
    },
  ```

  

### Update Todo

- updateTodoStatus action 함수 호출

  ```vue
  <template>
    <div>
      <div>
        <span :class="{ completed:todo.completed }" @click="updateTodoStatus">{{ todo.title }}</span>
        <button @click="deleteTodo(todo)">Delete</button>
      </div>
    </div>
  </template>
  
  <script>
  import { mapActions } from 'vuex'
  
  export default {
    ...
    props: {
      todo: Object,
    },
    methods: {
      ...
      updateTodoStatus: function () {
        this.$store.dispatch('updateTodoStatus', this.todo)
      },
    }
  }
  </script>
  ```

- Actions & Mutations

  ```js
    actions: {
      ...
      updateTodoStatus: function ({ commit }, todoItem) {
        commit('UPDATE_TODO_STATUS', todoItem)
      },
    },
  ```

  ```js
    mutations: {
      ...
      UPDATE_TODO_STATUS: function (state, todoItem) {
        // 배열의 각 요소에 함수를 적용 시킨 새로운 배열을 만들어서 state.todos에 할당
        state.todos = state.todos.map((todo) => {
          // 1. 클릭한 todoItem과 일치하는 state의 todo를 찾으면(업데이트 해줄 todo 찾기), 
          if (todo === todoItem) {
            // todo.completed = !todo.completed
            return {...todo, completed: !todo.completed}
          }
          // 클릭한 todoItem이 아니라면 원본 리턴
          return todo
        })
      }
    },
  ```

  

**JavaScript Spread Syntax**

- 전개 구문

- 반복 가능한 (iterable) 문자를 요소로 확장하여, 0개 이상의 key-value의 쌍으로 된 객체로 확장시킬 수 있음

- '...'을 붙여서 요소 또는 키가 0개 이상의 iterable object를 하나의 object로 간단하게 표현하는 법

- Spread Syntax의 대상은 반드시 iterable 객체여야 함

- 주 사용처

  1. 함수 호출
     - 배열의 목록을 함수의 인수로 활용 시
  2. 배열
  3. 객체
     - 객체 복사

  ```js
    mutations: {
      ...
      UPDATE_TODO_STATUS: function (state, todoItem) {
        // 배열의 각 요소에 함수를 적용 시킨 새로운 배열을 만들어서 state.todos에 할당
        state.todos = state.todos.map((todo) => {
          // 1. 클릭한 todoItem과 일치하는 state의 todo를 찾으면(업데이트 해줄 todo 찾기), 
          if (todo === todoItem) {
            // todo.completed = !todo.completed
            return {...todo, completed: !todo.completed}
          }
          // 클릭한 todoItem이 아니라면 원본 리턴
          return todo
        })
      }
    },
  ```



- v-bind를 사용한 class binding

  ```vue
  <template>
    <div>
      <div>
        <span :class="{ completed:todo.completed }" @click="updateTodoStatus(todo)">{{ todo.title }}</span>
        <button @click="deleteTodo(todo)">Delete</button>
      </div>
    </div>
  </template>
  
  ...
  <style scoped>
  .completed {
    text-decoration: line-through;
  }
  </style>
  ```

  

### Getters

- 완료된 todo 개수 계산

  ```js
  // index.js
    getters: {
      completedTodosCount: function (state) {
        return state.todos.filter((todo) => {
          return todo.completed === true
        }).length
      },
    }
  ```

  ```vue
  // App.vue
  
  <template>
    <div id="app">
      <h1>Todo List</h1>
      <h2>Completed Todo: {{ completedTodosCount }}</h2>
      <TodoList />
      <TodoForm />
    </div>
  </template>
  
  <script>
  ...
    computed: {
      completedTodosCount: function () {
        return this.$store.getters.completedTodosCount
      },
    }
  
  </script>
  ```

  





### Component Binding Helper

- JS Array Helper Method를 통해 배열 조작을 편하게 하는 것과 유사
  - 논리적인 코드 자체가 변함 x -> 쉽게 사용할 수 있도록 되어 있음에 초점

- 종류
  - mapState
  - mapGetters
  - mapActions
  - mapMutations

  

- mapState

  ```vue
  computed: {
    todos: function () {
      return this.$store.state.todos
    },
  }
  ```

  ↓ 수정 후

  ```vue
  import { mapState } from 'vuex'
  ...
  computed: {
    ...mapState(['todos',])
  }
  ```



- mapActions

  - 이전에 dispatch()를 사용했을 때 payload로 넘겨줬던 this.todo를 pass prop으로 변경해서 전달해야 함

  ```vue
  <template>
    <div>
      <div>
        <span :class="{ completed:todo.completed }" @click="updateTodoStatus(todo)">{{ todo.title }}</span>
        <button @click="deleteTodo(todo)">Delete</button>
      </div>
    </div>
  </template>
  
  <script>
  import { mapActions } from 'vuex'
  
  export default {
    ...
    methods: {
      ...mapActions([
        'deleteTodo',
        'updateTodoStatus',
      ])
    }
  }
  </script>
  ```

  

### LocalStorage

- session storage
  - 탭이 켜져있는 경우에만 저장 유지
- local storage
  - 사실상 영구 저장



쿠키 : 브라우저 종료시 삭제

세션 : 종료 시점 존재

로컬 스토리지 : 계속 남아있음



vuex-persistedstate

- 페이지가 새로고침 되어도 Vues state 유지시킴

- 설치 방법

  ```bash
  $ npm i vuex-persistedstate
  ```

- 라이브러리 사용

  ```js
  import createPersistedState from 'vuex-persistedstate'
  
  Vue.use(Vuex)
  
  export default new Vuex.Store({
    plugins: [
      createPersistedState(),
    ],
    ...
  ```
