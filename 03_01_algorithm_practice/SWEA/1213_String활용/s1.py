import sys
sys.stdin = open('input.txt', encoding='UTF8')

def BruteForce(pattern, text):
    i, j, cnt = 0, 0, 0
    m, n = len(pattern), len(text)
    while i < n:
        if text[i] != pattern[j]:
            i -= j
            j = -1
        i += 1
        j += 1
        if j == m:
            cnt += 1
            j = 0
    return cnt


for tc in range(1, 11):
    tc_num = int(input())
    word = input()
    sentence = input()
    ans = BruteForce(word, sentence)
    print('#{} {}'.format(tc, ans))

