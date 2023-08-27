n = int(input())
p = 1000-n
lst = [500, 100, 50, 10, 5]
answer = 0

for i in range(5):
    if p == 0:
        break
    if p >= lst[i]:
        answer += p//lst[i]
        p = p%lst[i]

if p: answer += p
print(answer)