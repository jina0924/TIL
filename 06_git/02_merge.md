# Merge

[toc]

## Branch Merge

### git merge

- `git merge 병합할브랜치이름`
  - 주의사항: merge하기 전에 일단 다른 브랜치를 합치려고 하는 브랜치(메인 브랜치)로 switch 해야함

```bash
# 1. 현재 branch1과 branch2가 있고, HEAD가 가리키는 곳은 branch1
$ git branch
* branch1
  branch2

# 2. branch2를 branch1에 합치려면?
$ git merge branch2

# 3. branch1을 branch2에 합치려면?
$ git switch branch2
$ git merge branch1
```



### Merge의 세 종류

#### 1. Fast-Forward(빨리감기)

> 브랜치를 병합할 때 빨리감기처럼 브랜치가 가리키는 커밋을 앞으로 이동시키는 것

```bash
$ git switch -c 새브랜치
$ touch login.txt
$ git add .
$ git commit -m '커밋메시지'
$ git log --oneline --all	# master / HEAD-> login
$ git switch master		#master브랜치로 옮겨감 why? 여기다 merge하기 위해
$ git merge login		# Fast-forward 뜸 & login에서 만든 login.txt생김
```

메인브랜치에 아무런 변화 없이 새 브랜치에 커밋이 쌓였을 때 메인브랜치가 새 브랜치 커밋으로 나아감

※ 머지된 브랜치 : 해당 브랜치의 역할은 끝남 -> 머지된 브랜치 삭제할 것



#### 2. 3-Way Merge(Merge commit)

> 브랜치를 병합할 때 각 브랜치의 커밋 두개와 공통 조상 하나를 사용하여 병합하는 것
>
> - 두 브랜치의 공통 조상 커밋 + 메인 브랜치 커밋 + 서브 브랜치 커밋 => 새 커밋 생성
>
> 두 브랜치에서 다른 파일 혹은 같은 파일의 다른 부분을 수정했을 때 가능

```bash
$ git switch -c signout
...
$ git commit -m '커밋메시지'
$ git switch master
...
$ git commit -m '커밋메시지'
$ git log --oneline --all --graph
* c851530 (HEAD -> master) master test 2
| * a118419 (signout) signout test 1
|/
* 68ba94d login test 1
* b2d5ce9 master test 1
$ git merge signout
Merge made by the 'ort' strategy.
 signout.txt | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 signout.txt
$ git log --oneline --all --graph
*   6bdf8df (HEAD -> master) Merge branch 'signout'
|\
| * a118419 (signout) signout test 1
* | c851530 master test 2
|/
* 68ba94d login test 1
* b2d5ce9 master test 1
$ git branch -d signout
```

- 별도로 지정하지 않아도 merge commit 자동 생성



#### 3. Merge Conflict(충돌 상황)

> 병합하는 두 브랜치에서 같은 파일의 같은 부분을 수정한 경우
>
> Git은 해당 부분을 자동으로 merge해주지 못함
>
> => 사용자가 직접 내용을 선택해서 Conflict를 해결해야 함

```bash
$ git switch -c hotfix
...
$ git commit -m 'hotfix test 1'
$ git log --oneline --all --graph
* 5d395db (HEAD -> hotfix) hotfix test 1
*   6bdf8df (master) Merge branch 'signout'
|\
| * a118419 signout test 1
* | c851530 master test 2
|/
* 68ba94d login test 1
* b2d5ce9 master test 1
$ git switch master
...
$ git commit -m 'master test 3'
$ git log --oneline --all --graph
* 2ff8291 (HEAD -> master) master test 3
| * 5d395db (hotfix) hotfix test 1
|/
*   6bdf8df Merge branch 'signout'
|\
| * a118419 signout test 1
* | c851530 master test 2
|/
* 68ba94d login test 1
* b2d5ce9 master test 1
$ git merge hotfix
Auto-merging test.txt
CONFLICT (content): Merge conflict in test.txt
Automatic merge failed; fix conflicts and then commit the result.
$ git status
	both modified:   test.txt
$ git add .
$ git commit	# 커밋메시지 따로 작성하지 않음
# vim 에디터 켜짐(마우스 쓸 수 없음)
# Merge branch 'hotfix' - 자동으로 작성된 커밋 메시지
# 수정을 마치거나 수정할 것이 더 이상 없을 경우 : esc + :wq + enter
$ git log --oneline --all --graph
*   d21c88c (HEAD -> master) Merge branch 'hotfix'
|\
| * 5d395db (hotfix) hotfix test 1
* | 2ff8291 master test 3
|/
*   6bdf8df Merge branch 'signout'
|\
| * a118419 signout test 1
* | c851530 master test 2
|/
* 68ba94d login test 1
* b2d5ce9 master test 1
$ git branch -d hotfix
```

※ checkout -> switch + restore로 분화됨