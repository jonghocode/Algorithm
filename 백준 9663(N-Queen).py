n = int(input())
chk = [0]*20; lchk = [0]*40; rchk = [0]*40 # 열, 왼쪽 대각선, 오른쪽 대각선

def queen(d):
    global answer
    if d == n:
        answer+=1
        return
    for i in range(n):
        if chk[i] + lchk[d-i+n] + rchk[d+i] == 0:
            chk[i] = 1
            lchk[d-i+n] = 1
            rchk[d+i] = 1
            queen(d+1)
            chk[i] = 0
            lchk[d-i+n] = 0
            rchk[d+i] = 0


answer = 0
queen(0)
print(answer)