# 10828 스택
from sys import stdin
n = int(input())

my_stack = []

for i in range(n):
    command = stdin.readline().split()
    if command[0] == 'push':
        my_stack.append(command[1])
    elif command[0] == 'pop':
        if len(my_stack) == 0:
            print(-1)
        else:
            print(my_stack.pop())
    elif command[0] == 'size':
        print(len(my_stack))
    elif command[0] == 'empty':
        if len(my_stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(my_stack) == 0:
            print(-1)
        else:
            print(my_stack[-1])