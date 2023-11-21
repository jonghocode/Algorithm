# 사용할 문제 2문제 이상
# 합 l보다 크거나 같고, r보다 작거나 같음
# 쉬운 문제 어려운문제 차이 x 보다 크거나 같아야 함

def back(d, sum, idx):
    global answer
    if sum > r:
        return
    # 처음에 lst를 정렬 했으므로 -1 과 0을 비교하면된다.
    if d >= 2 and l<= sum <= r and temp[-1] - temp[0] >= x:
        answer += 1

    # idx 매개 변수를 이용해서 중복 체크를 한다.
    for i in range(idx, n):
        temp.append(lst[i])
        back(d+1, sum+lst[i], i+1)
        temp.pop()

n, l, r, x = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
temp = []
answer = 0

back(0, 0, 0)
print(answer)