duck = input()
if len(duck) % 5 != 0:
    print(-1)
    exit()

chk = [0]*len(duck)
lst = ['q', 'u', 'a', 'c', 'k']

answer = 0
for i in range(len(duck)):
    if chk[i] == 1:
        continue

    cnt = 0
    p = 0
    if duck[i] == 'q':
        for j in range(i, len(duck)):
            if lst[p] == duck[j] and chk[j] == 0:
                chk[j] = 1
                p += 1
                cnt+=1
            if p == 5:
                p = 0
        if cnt % 5 != 0:
            print(-1)
            exit()

    answer += 1

for i in range(len(chk)):
    if chk[i] == 0:
        answer = -1

print(answer)