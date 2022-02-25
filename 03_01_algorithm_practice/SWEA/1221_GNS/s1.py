import sys
sys.stdin = open('input.txt')

# 문자와 숫자를 대응시킨 딕셔너리 만들어줌
num_dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
# 나중에 숫자에 대응한 문자를 찾기 위해 key와 value값을 뒤집은 딕셔너리도 마련함
reversed_num_dict = {v: k for k, v in num_dict.items()}
T = int(input())

for tc in range(1, T+1):
    tc_num, length = input().split()
    n = int(length)
    str_nums = list(input().split())
    int_nums = [0] * n              # 문자 리스트를 숫자로 변환해서 담을 곳 마련
    sorted_str_nums = [0] * n       # 최종적으로 정렬된 문자 리스트를 담을 곳
    for i in range(n):              # 입력받은 문자 리스트 요소를 키 값으로 하여 그에 해당하는 숫자를 담음
        int_nums[i] = num_dict.get(str_nums[i])
    int_nums.sort()                 # 숫자 리스트 정렬
    for j in range(n):
        sorted_str_nums[j] = reversed_num_dict.get(int_nums[j])   # 숫자를 키 값으로 해서 해당하는 문자 찾아서 담음

    print('#{}'.format(tc))
    print(*sorted_str_nums)

