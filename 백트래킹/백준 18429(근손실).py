n, k = map(int, input().split())
lst = list(map(int, input().split()))
chk = [0]*n
answer = 0
def health(d, sum):
    global answer

    if sum < 500:
        return
    if d == n:
        answer += 1
        return
    
    for i in range(n):
        if chk[i] == 0:
            chk[i] = 1
            health(d+1, sum+lst[i]-k)
            chk[i] = 0
    
health(0, 500)
print(answer)
