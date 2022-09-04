# mirror

[toc]

## 1. BFG Repo-Cleaner 다운

https://rtyley.github.io/bfg-repo-cleaner/



## 2. java 다운

> BFG Repo-Cleaner 사용을 위해 자바 필요

https://projects.eclipse.org/projects/adoptium.temurin



## 3. 기반 작업

1. 새 Repo 생성
2. default branch 이름 target repo와 맞추기
3. target repo의 branch protect 해제



## 4. BFG Repo-Cleaner 100MB이상 대용량 히스토리 정리

1. target repo의 http 주소 복사

2. 임의의 폴더 생성하고 클론하기

   ```bash
   $ git clone --mirror <gitlab 주소>
   # $ git clone --mirror https://lab.ssafy.com/s07-webmobile3-sub2/S07P12A109.git
   ```

3. 같은 디렉토리에 1에서 다운받은 `bf-1.14.0.jar` 파일을 위치시킴

4. 대용량 파일 삭제

   ```bash
   S07P12A109.git 과 같은 레벨에 bfg-1.14.0.jar 위치시키기
   $ java -jar bfg-1.14.0.jar --strip-blobs-bigger-than 100M <gitlab 폴더>
   # $ java -jar bfg-1.14.0.jar --strip-blobs-bigger-than 100M S07P12A109.git/
   ```

   ![img](https://cdn.discordapp.com/attachments/1015975060172984340/1015977585026551818/unknown.png)

5. 삭제 내용 적용

   ```bash
   깃랩폴더로 이동 (이후 계속 깃랩폴더 안에서 진행)
   $ cd <깃랩폴더>
   # $ cd S07P12A109.git
   
   $ git reflog expire --expire=now --all && git gc --prune=now --aggressivexxxxxxxxxx 깃랩폴더로 이동 (이후 계속 깃랩폴더 안에서 진행)$ cd <깃랩폴더># $ cd S07P12A109.git$ git reflog expire --expire=now --all && git gc --prune=now --aggressive
   ```

   ![img](https://cdn.discordapp.com/attachments/1015975060172984340/1015977694099419136/unknown.png)



## 5. 새로운 저장소로 push

1. target repo의 `user.name`과 `user.email`을 new repo의 것으로 변경

   - 확인 방법

     ```bash
     유저네임, 유저이메일 확인하기
     $ git config user.name
     $ git config user.email
     ```

     ![img](https://cdn.discordapp.com/attachments/1015975060172984340/1015977780342698099/unknown.png)

   - 이름, 이메일 주소 변경

     ```bash
     $ git filter-branch -f --env-filter "GIT_AUTHOR_NAME='깃허브 작성자 이름'; GIT_AUTHOR_EMAIL='깃허브 작성자 이메일'; GIT_COMMITTER_NAME='깃허브 작성자 이름'; GIT_COMMITTER_EMAIL='깃허브 작성자 이메일';" HEAD
     ```

     ![img](https://cdn.discordapp.com/attachments/1015975060172984340/1015977917135724574/unknown.png)

2. 새 저장소에 반영

   ```bash
   $ git push --mirror <github 주소>
   ```

   ![img](https://cdn.discordapp.com/attachments/1015975060172984340/1015978036061016124/unknown.png)

