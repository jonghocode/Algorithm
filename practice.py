# 백준 2346(풍선 터뜨리기)

n = int(input())
lst = [i for i in range(1, n+1)]
temp = [0] + list(map(int, input().split()))
st, answer = temp[1], [1]

for i in range(1, n):
    cnt = 0
    if st > 0:
        while True:
            x = lst.pop(0)
            cnt += 1
            if cnt != st:
                lst.append(x)
    else:
        while True: