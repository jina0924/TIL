# 2869번 달팽이는 올라가고 싶다

a, b, v = map(int, input().split())
up = a - b

if (v-b) % up == 0:
    print((v-b) // up)
else:
    print((v-b) // up + 1)