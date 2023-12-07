n, k = map(int, input().split())
s = []
for i in range(n):
    s.append('B')

sum, acnt, T = 0, 0, n
flag = False
for i in range(n):
    now = -1
    sw = i
    for j in range(n-1, -1, -1):
        if s[j] == 'A':
            break
        now += 1
        if now + sum == k:
            sw = j
            flag = True
            break

        # print(s, sum, now, j)
    s[sw] = 'A'

    if now+sum == k:
        flag = True
        break
    acnt += 1 # A개수
    T -= 1 # B개수
    sum = T*acnt-acnt # 9 88 777 # A가 하나 더 생길때마다 그 전 A의 개수는 하나 줄어든다.
    # print(s, sum)
if flag:
    print(''.join(map(str, s)))
else:
    print(-1)
