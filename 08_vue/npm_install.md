# npm install

npm install의 동작

1. 패키지명을 명시해 특정 패키지를 설치하는 동작

   ```bash
   $ npm install -g @vue/cli
   ```

   - vue 설치

2. 패키지명을 명시하지 않고 `package.json`파일의 의존성을 설치하는 동작

   ```bash
   $ npm install
   ```

   - package.json에 저장된 모든 패키지 설치