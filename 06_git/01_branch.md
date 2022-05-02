# Branch

[toc]

## Branch

- 나뭇가지처럼 여러 갈래로 작업 공간 나누어 독립적으로 작업할 수 있도록 도와주는 Git의 도구



### branch command

#### git branch

> 브랜치 조회, 생성, 삭제 등 브랜치와 관련된 Git 명령어

- `git branch` : 브랜치 목록 확인
- `git branch 브랜치이름` : 새로운 브랜치 생성
- `git branch -d 브랜치이름` : 특정 브랜치 삭제(병합된 브랜치만 삭제)
- `git branch -D 브랜치이름` : 강제 삭제(병합되지 않은 브랜치도 삭제 가능)



#### git switch

> 현재 브랜치에서 다른 브랜치로 HEAD를 이동시키는 명령어
>
> - HEAD : 현재 브랜치를 가리키는 포인터

- `git switch 브랜치이름` : 해당 브랜치 이동
  - 주의사항 : git add하지 않은 새로운 파일은 git의 버전관리를 받고 있지 않으므로 브랜치를 변경해도 영향x
- `git switch -c 브랜치이름` : 브랜치를 새로 만들고 이동



#### check branch

- `git log --oneline --all` : HEAD와 상관없이 모든 commit 볼 수 있음(oneline과 all 순서 상관x)
- `git log --oneline --all --graph` : 브랜치 갈라진 모습 볼 수 있음



## Branch scenario

```bash
$ git init

# 브랜치 목록 확인
$ git branch(아직 아무것도 안뜸)
$ touch test.txt
$ git status
$ git add .
$ git commit -m '커밋메시지'
$ git log(계정 정보까지)
$ git log --oneline(한줄로)

# login 브랜치 생성
$ git branch login
$ git branch	# master, login이 같은 곳 가리키고 있음
$ git add .
$ git commit -m '커밋메시지'
$ git log --oneline		#master하나 앞으로 나감 & HEAD/login은 그대로
$ git switch login
$ git log --oneline		# HEAD->login
$ git log --oneline --all	# master / HEAD-> login
파일 추가
$ git log --oneline --all() --graph
$ git switch master
$ git branch -d login(삭제 안됨: 'login' is not fully merged)
```