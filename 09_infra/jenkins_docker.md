# CI / CD 구축

0. Docker 설치

   - https://docs.docker.com/get-docker/

   - command창

     ```bash
     C:\Users\g>docker --version
     Docker version 20.10.16, build aa7e414
     ```

1. Docker로 Jenkins를 설치

   - command창

     ```bash
     docker run -d -p 9090:8080 -p 50000:50000 -v /var/jenkins:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock --name jenkins -u root jenkins/jenkins:lts-jdk11
     ```

   - http://localhost:9090/ 접속 후 설정

     - admin 비밀번호

       ```bash
       C:\Users\g>docker logs jenkins
       ```

       별 무더기 사이에 비밀번호 나옴

2. Jenkins 플러그인 설치

   - DashBoard > Manager Jenkins > Plugin Manager
   - Gitlab, Docker 플러그인 설치

3. Jenkins 컨테이너 안 도커 설치

   - command창

     ```bash
     C:\Users\g>docker exec -it jenkins bash
     root어쩌고# curl https://get.docker.com/ > dockerinstall && chmod 777 dockerinstall && ./dockerinstall
     root어쩌고# docker --version
     Docker version 20.10.17, build 100c701
     ```

4. 도커라이징 및 배포 설정

   - 배포하려는 레포지토리에 Dockerfile파일 추가

     ```dockerfile
     # build stage
     FROM node:lts-alpine as build-stage
     WORKDIR /app
     COPY package*.json ./
     RUN npm install
     COPY . .
     RUN npm run build
     
     # production stage
     FROM nginx:stable-alpine as production-stage
     COPY --from=build-stage /app/dist /usr/share/nginx/html
     EXPOSE 80
     CMD ["nginx", "-g", "daemon off;"]
     ```

   - Dashboard > 새로운 Item > 프로젝트명 작성 > Freestyle project 선택

   - 소스 관리 > Git 선택 > Repository URL에 배포대상 git 주소 복붙 

   - Credentials에서 Username에 gitlab 아이디, password에 비밀번호 작성

   - Build Triggers에 Build when a change is pushed ~ 체크 및 필요한 다른 옵션 체크

   - Build > Execute shell 선택

     ```tex
     docker build -t front:0.1 .
     docker run -d -p 80:80 front:0.1
     ```

     작성 후 저장

5. 빌드 및 배포

