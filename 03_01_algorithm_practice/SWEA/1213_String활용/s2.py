# 1213 String활용
import sys
sys.stdin = open('input.txt', encoding='UTF8')

def BruteForce(pattern, text):
    m, n = len(pattern), len(text)
    cnt = 0
    for i in range(n-m+1):
        for j in range(m):
            if text[i] != pattern[j]:
                break
            i += 1
        else:
            cnt += 1
    return cnt

for tc in range(1, 11):
    tc_num = int(input())
    word = input()
    sentence = input()
    ans = BruteForce(word, sentence)
    print('#{} {}'.format(tc, ans))

