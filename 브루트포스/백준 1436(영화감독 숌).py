n = int(input())
answer, start = 0, 665

while answer != n:
    start += 1
    temp = start
    while temp != 0:
        if temp % 1000 == 666:
            answer += 1
            break
        else:
            temp //= 10

print(start)