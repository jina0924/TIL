# SWEA 5432. 쇠막대기 자르기

class Cut:
    def __init__(self, data):
        self.stack = []
        self.stick = 0
        self.data = data

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def check_stick(self):
        for i in range(len(self.data)):
            if self.data[i] == '(':
                self.push(self.data[i])
                self.stick += 1
            elif self.data[i] == ')':
                if self.data[i-1] == '(':
                    self.stick -= 1
                    self.pop()
                    self.stick += len(self.stack)
                else:
                    self.pop()
        return self.stick

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    position = list(input())
    laser_cut = Cut(position)
    ans = laser_cut.check_stick()
    print('#{} {}'.format(tc, ans))

