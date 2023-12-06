n, k = map(int, input().split())
s = []
for i in range(n):
    s.append('B')

sum, acnt = 0, 0
for i in range(n):
    now = 0
    sw = 0
    for j in range(n-1, -1, -1):
        if s[j] == 'A':
            break
        now += 1
        s[j] = "A"
        if now != k:
            s[j] = 'B'
        else:
            sw = 1
            break
    if sw == 0:
        s[i] = 'A'
    acnt += 1
    sum += now
    sum -= acnt
    print(s, sum)
print(s)