# Git - 심화

[toc]

## Undoing

### 1. 파일 내용을 수정 전으로 되돌리기

- Modified 파일 되돌리기
- Working Directory에서 파일을 수정했다고 가정



#### (1) git restore

- `git restore <파일 이름>`
- git이 추적하고 있는(버전 관리가 되고 있는) 파일만 되돌리기 가능
- 수정했던 내용 전부 사라짐 ->  복원 불가능



### 2. 파일 상태를 Unstage로 되돌리기

- Staging Area와 Working Directory 사이를 넘나드는 방법
- git add를 통해서 파일을 Staging Area에 올렸다고 가정



#### (1) git rm --cached

- `git rm --cached <file>`

- 기존에 커밋이 없는 경우



#### (2) git restore --staged

- `git restore --staged <file>`

- 기존에 커밋이 존재하는 경우



### 3. 바로 직전 완료한 커밋 수정하기

#### (1) git commit --amend

- 상황별 2가지 기능
  1. 커밋 메시지만 수정
     - 마지막으로 커밋하고나서 수정한 것이 없을 때
  2. 이전 커밋 덮어쓰기
     - Staging Area에 새로 올라온 내용이 있을 때



**[참고] vim**

- `i` : 입력 상태 바꿈 (끼워 넣기 활성화 & 커서 생김)
- `esc` : 입력 모드 나감
- `:wq + enter` : 저장



### 4. 특정 커밋 메시지 수정하기

1. 변경하고 싶은 커밋으로 이동

   ```bash
   $ git rebase -i <해시코드>
   ```

2. 수정하고 싶은 커밋에 `pick` -> `reword`로 변경 후 메시지 변경 및 저장



## Reset & Revert

> 공통점
>
> - 과거로 되돌림
>
> 차이점
>
> - 과거로 되돌리겠다는 내용도 기록되는가(== commit 이력에 남는가)

### 1. git reset

```bash
$ git reset [옵션] <커밋 ID>
```

- 특정 커밋으로 되돌아 갔을 때, 해당 커밋 이후로 쌓아 놨던 커밋들은 전부 사라짐



**옵션**

- 생략 시 `--mixed`가 기본 값

1. `--soft`
   - 이후의 commit된 파일들을 staging area로 돌려놓음 (commit 하기 전 상태)
2. `--mixed`
   - 이후의 coomit된 파일들을 working directory로 돌려놓음 (add 하기 전 상태)
3. `--hard`
   - 이후의 commit된 파일들(tracked 파일들)은 모두 working directory에서 삭제
   - 단, Untracked 파일은 그대로 Untracked로 남음



**[참고 사항]**

혹시 이미 삭제한 커밋으로 다시 되돌아가고 싶다면 -> `git reflog`



### 2. git revert

```bash
$ git revert <커밋 ID>
```

- 특정 사건을 없었던 일로 만드는 행위
- 이전 커밋을 취소한다는 새로운 커밋을 만듦
- reset과 revert의 차이점
  - `git reset` : 커밋 내역을 삭제
  - `git revert` : 새로운 커밋을 쌓음



**[참고 사항]**

```bash
# 공백을 통해 여러 커밋을 한꺼번에 되돌리기 가능
$ git revert 7f6c24c 006dc87 3551584

# 범위 지정을 통해 여러 커밋을 한꺼번에 되돌리기 가능
$ git revert 3551584..7f6c24c

# 커밋 메시지 작성을 위한 편집기를 열지 않음 (자동으로 커밋 완료)
$ git revert --no-edit 7f6c24c

# 자동으로 커밋하지 않고, Staging Area에만 올림 (이후, git commit으로 수동 커밋)
# 이 옵션은 여러 커밋을 revert 할 때 하나의 커밋으로 묶는게 가능
$ git revert --no-commit 7f6c24c
```



## Git workflow

### 1. Feature Branch Workflow

> 서로 저장소의 소유권이 있는 경우

개발은 master에서 진행 x -> feature에서 진행

- master는 최종적으로 병합시에만 사용



과정

1. 1번 유저 : git push origin feature/login
2. master 브랜치로 병합
3. 각 유저가 master 브랜치 pull 받기
4. 병합 완료된 feature/~~ 브랜치 삭제



- 1번 유저가 깃헙에서 new repository 생성

- setting에서 collaborator 추가
  - 2번 유저에게 메일 날라감 -> 승인 해야함
- 2번 유저가 clone 받음
- $ git switch -c feature/login (브랜치 생성하면서 이동)
- $ git push origin feature/login
- 1번 유저한테 알림 감(compare & pull request)
- Open a pull request(1번유저, 2번 유저 모두 가능)
- 2번 유저가 create pull request
- 1번 유저가 코드 비교해야 함 -> Commits / Files changed => Merge pull request(오류 없는 경우 병합) / Close pull request(잘못된 경우 닫기)
  - 코드에 마우스 오버하면 + 버튼 생김 -> Add a suggestion -> start a review
  - 빨간색을 초록색으로 변경할 것을 제안(빨간색 없어지지 x)
  - finish your review
  - Commit suggestion클릭하면 review한 코드 반영됨
  - merge pull request는 권한을 제한할 수 있음(ex. 팀장 세 명이 모두 review해야 함)
  - Confirm merge
  - delete branch
- merge 후 2번 유저
  - $ git switch master
  - $ git pull origin master
  - $ git branch -d feature/login



### 2. Forking Workflow

> 저장소의 소유권이 없는 경우 ex) 오픈 소스

- 원본을 Fork(복제)

- 복제한 것을 clone

- $ git remote add upstream [원본 URL]
- 브랜치에서 개발
- 기능 구현 후 원격 저장소(복제본)에 브랜치 반영
- pull reqeust
- 원본에서 병합했다면 master브랜치로 switch(pull 받음(?))
  - $ git pull upstream master
- 원격 저장소에서 병합 완료 된 로컬 브랜치 삭제



- 1번 유저: 오픈소스 소유주

- 2번 유저가 fork
- 복제한(fork)것 clone
- $ git remote -v
  - 현재 복제된 주소만 있음
- $ git remote add upstream 원본저장소_주소
- $ git switch -c feature/login
- 개발개발
- $ git push origin feature/login
- 2번 유저가 pull request 만듦
  - merge 버튼 없음
- 1번 유저한테 pull request 생김
- ...
- 2번 유저 $ git switch master
- $ git pull upstream master(내 브랜치 말고 원본에 반영됐으므로)