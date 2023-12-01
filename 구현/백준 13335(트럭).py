n, w, l = map(int, input().split())
car = list(map(int, input().split()))
lst = []
idx, sum, cnt, answer = 0, 0, 0, 0

while True:
    if idx >= n and len(lst) == 0:
        break
    
    for i in range(len(lst)): # 이동하기
        lst[i][1] += 1
    
    if len(lst) and lst[0][1] > w: # 다리를 건넜다면 빼기
        weight, time = lst.pop(0)
        sum -= weight; cnt -= 1;

    if idx < n and sum + car[idx] <= l and cnt < w: # 넣기
        lst.append([car[idx], 1])
        sum += car[idx]; cnt += 1; idx += 1

    answer += 1

print(answer)