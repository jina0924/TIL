# Vue2와 Vue3 차이

[toc]

## v-model

- 커스텀 컴포넌트를 사용할 때, `v-model` prop와 event 기본 명칭이 변경됨
  - prop : `value` → `modelValue`
  - event : `input` → `update:modelValue`
- `v-bind` 의 `.sync` 수식어와 컴포넌트의 `model` 옵션이 제거되고 `v-model` 전달인자로 대체됨
- 동일 컴포넌트에서 다중의 `v-model` 바인딩 가능
- 사용자 지정 `v-model` 수식어를 생성하는 기능 추가 



## key 속성

- Vue가 고유한 key를 자동으로 생성
  - `v-if`, `v-else`, `v-else-if` 에서 더 이상 key 필요 x
  
  - 수동으로 key를 정할 경우, 반드시 고유한 key를 사용해야 함 (의도적으로 동일한 key를 사용하여 분기를 강제로 재사용할 수 없음)
  
  - `<template v-for>` 의 key는 자식이 아닌 `<template>` 태그에 있어야 함
  
    ```vue
    <template v-for="item in list" :key="item.id">
      <div>...</div>
      <span>...</span>
    </template>
    ```
  
    



## v-if 와 v-for의 우선 순위

동일한 엘리먼트에 `v-if`와 `v-for`를 함께 사용할 때, `v-if`가 더 높은 우선순위를 가짐



## v-bind 병합 동작

> v-bind의 바인딩 순서가 렌더링 결과에 영항을 미침

- 2.x 구문

  ```vue
  <!-- 템플릿 -->
  <div id="red" v-bind="{ id: 'blue' }"></div>
  <!-- 결과 -->
  <div id="red"></div>
  ```

  - `v-bind` 와 개별 속성이 모두 정의된 경우, 개별 속성이 항상 object의 바인딩을 덮어씀

- 3.x 구문

  ```vue
  <!-- 템플릿 -->
  <div id="red" v-bind="{ id: 'blue' }"></div>
  <!-- 결과 -->
  <div id="blue"></div>
  
  <!-- 템플릿 -->
  <div v-bind="{ id: 'blue' }" id="red"></div>
  <!-- 결과 -->
  <div id="red"></div>
  ```

  - `v-bind` 와 개별 속성이 모두 정의된 경우, 바인딩 순서에 따라 병합 방법이 결정됨
  - 개별 속성와 `v-bind` 속성 선언 순서 유의할 것 (마지막에 선언한 값으로 병합)