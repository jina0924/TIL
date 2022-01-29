n = int(input())
numbers = list(map(int, input().split()))

if 1 in numbers:
    numbers.remove(1)

for i in range(2, 1001):
    for num in numbers:
        if num % i == 0 and i != num:
            numbers.remove(num)

print(len(numbers))