# Dynamic Programming(동적 계획법)

[toc]

## 개요

- 하나의 큰 문제를 여러 개의 작은 문제로 나누어서 그 결과를 저장하여 다시 큰 문제를 해결할 때 사용
- '기억하며 풀기'



## DP 사용 조건

1. Overlapping Subproblems(겹치는 부분 문제)
   - 동일한 작은 문제들이 반복하여 나타나는 경우
   - 부분 문제를 재활용할 수 있는지 여부
2. Optimal Substructure(최적 부분 구조)
   - 부분 문제의 최적 결과 값을 사용해 전체 문제의 최적 결과를 낼 수 있는 경우



## DP 사용

1. DP로 풀 수 있는 문제인지 파악
   - DP 사용 조건을 충족하는 문제인가
2. 문제의 변수 파악
3. 변수 간 관계식 만들기(점화식)
   - ex) `f(n) = f(n-1) + f(n-2)`
4. 메모(memoization or tabluation)
   - 변수의 값에 따른 결과를 저장
5. 기저 상태 파악
   - 가장 작은 문제의 상태를 알아야 함
   - ex) 피보나치 수열에서 `f(0) = 0`,  `f(1) = 1`
6. 구현
   - Bottom-Up(Tabulation방식) - 반복문 사용
   - Top-Down(Memoization방식) - 재귀 사용