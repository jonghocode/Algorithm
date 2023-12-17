# 백준 2295(세수의 합)

더한 딕셔너리
2, 3 = 5
2, 5 = 7
2, 10 = 12
3, 5 = 8
3, 10 = 13
5, 10 = 15

뺀 딕셔너리
2, 3 = 1
2, 5 = 3
2, 10 = 8
2, 18 = 16
3, 5 = 2
3, 10 = 7
3, 18 = 15
5, 10 = 5
5, 18 = 13
10, 18 = 8

현재 고른 더한 딕셔너리에서 고른 두 수를 제외하고 뺀 딕셔너리에서
제일 큰 값(뒤 값이 큰 값 중 제일 큰 값)을 찾아야 함

시간 복잡도 : nlog(n)


# 백준 2295(세수의 합)

n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()
add, minus = {}, {}

for i in range(n-1): # 더하는 딕셔너리
    for j in range(i+1, n-1):
        temp = lst[i] + lst[j]
        if temp not in add:
            add[temp] = []
            add[temp].append([i, j])
        else:
            add[temp].append([i, j])

for i in range(n): # 빼는 딕셔너리
    for j in range(i+1, n):
        temp = lst[j] - lst[i]
        if temp >= 0:
            if temp not in minus:
                minus[temp] = []
                minus[temp].append([i, j])
            else:
                minus[temp].append([i, j])

for key, value in add.items():
    for t in value:
        x, y = t[0], t[1]
        
        if key in minus:
            l, r = 0, len(minus[key])    
            
            while l <= r:
                mid = (l + r) // 2