# 각 계란의 내구도는 상대의 무게만큼 깎임
def go(d, sum, idx):
    global answer
    # print(f"answer : {answer}, d : {d}, sum : {sum}, idx : {idx}, lst : {lst}")
    if d == n:
        answer = max(answer, sum)
        return
    
    for i in range(idx, n): # 오른쪽에 있는 계란 잡기
        if lst[i][0] > 0:
            st, weight = lst[i][0], lst[i][1]
            sw = 0
            for j in range(n):
                cnt = 0
                if i != j and lst[j][0] > 0:
                    st2, weight2 = lst[j][0], lst[j][1]
                    lst[i][0] -= weight2
                    lst[j][0] -= weight
                    if lst[i][0] <= 0:
                        cnt += 1
                    if lst[j][0] <= 0:
                        cnt += 1
                    go(d+1, sum+cnt, i+1)
                    lst[i][0] = st
                    lst[j][0] = st2
                    sw = 1
            if sw == 0: # 고를 계란이 없다면 그냥 넘어가기
                go(d+1, sum, i+1)
        else: # 오른쪽에 있는 계란을 잡았는데 깨져있다면 넘어가기
            go(d+1, sum, i+1)
            
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
chk = [0]*n
answer = -1
go(0, 0, 0)
print(answer)