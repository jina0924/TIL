# Git & GitHub

[toc]

## Git

### 1. Working Directory

1. `git init` : 최초 1번만 실행. 버전 관리를 하고 싶은 최상단에 단 한 번
   - 해당 폴더에 `.git` 이라는 숨긴 폴더 생성
   - `master` 라고 하는 사인이 우측에 나타남 
2. `touch 파일명` : 파일 생성
3. `git status` : WD / SA 상태를 확인하는 명령어
   - 빨간색 : WD
   - 초록색 : SA
4. `git config --global --list` : 세팅 확인하는 방법

### 2. Staging Directory

1. `git add 파일명` : 파일을 스테이지에 올림
1. `git add .` : 현재 디렉토리의 모든 파일이 스테이징
2. `git status`

### 3. Commits

- snapshot을 찍는 것 -> 현재 상태를 하나의 버전으로 남기는 것
- 누가  / 어떤 것을 수정해서 버전으로 남겼는지 확인 가능

1. `git config --global user.email "메일주소"`
2. `git config --global user.name "자기 이름"`
3. `git commit -m "커밋메시지"`
4. `git log` : commit 메시지를 확인하는 명령어
   - `git log --oneline` : log를 간소화해서 볼 수 있음



## GitHub

### 0. 원격저장소 생성

- 우측 상단 `+` 클릭 -> New repository
  - Public : 전체 공개
  - Private : 나 + 허용한 사람만

### 1. Commits

- `git remote add origin [원격 URL]` : 로컬 저장소와 원격 저장소 연결
  - origin이란 이름은 바꿔도 되지만 일반적으로 많이 사용
  - 원격저장소 이름을 'origin'으로 지은 것

- `git remote -v` : 주소 등록 확인

- `git remote rm origin` : 원격저장소 이름을 지움

### 2. 파일

- `git push origin master` : origin이란 master브랜치에 push함
  - 커밋 새로 찍어도 자동 동기화 되지 x 
  - commit 이라는 변경 사항에 대한 기록을 기반으로 동작

### 3. Clone 

원격저장소에서 모든 내역을 가져옴
최초 한 번만 수행함 -> 그 이후로는 pull만 하면 됨

1. 초록색 Code 클릭 -> 주소 복사
2. `git clone 주소`
   - 폴더 이름은 바꿔도 상관 없음
   - GitLab에서 clone할 땐 https 주소 가져오기

### 4. Pull

- 원격저장소에 있는 커밋 내용을 로컬저장소로 당겨옴
  1. git pull origin master



## .gitignore

> 특정 파일 혹은 폴더에 대해 Git이 버전 관리를 하지 못하도록 지정

### 1. .gitignore  작성 시 주의 사항

- 반드시 이름을 `.gitignore`로 작성해야 함

- `.gitignore`파일은 `.git` 폴더와 동일한 위치에 생성

- **제외하고 싶은 파일은 반드시 commit하기 전에 `.gitignore`에 작성**

  - add가 이미 됐으면 동작하지 않음

  - `git init` 하는 순간 동시에 만들 것

    ex) `*.txt` : 텍스트 파일은 전부 무시됨
    ex) `venv/` : 폴더 안 모든게 무시됨



### 2. gitignore.io

https://www.toptal.com/developers/gitignore

.gitignore의 내용을 쉽게 작성할 수 있도록 도와주는 두 개의 사이트를 소개

자신의 개발 환경에 맞는 것을 찾아서 전체 복사, 붙여넣기