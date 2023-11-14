n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
mx = [0] * n
mx[0] = a[0]
for i in range(1, n):
    mx[i] = mx[i - 1] + a[i]
    
evt = []
T = []
for _ in range(m):
    l, r = map(int, input().split())
    T.extend([l, r + 1])
    evt.extend([(l, 1), (r + 1, -1)])
    
T = list(set(T))
T.sort()
    
p = 0
ans = 0
ans2 = 0
    
T.append(T[-1] + 1)
    
j = 0
for t in range(len(T) - 1):
    added = 0
    removed = 0
        
    while j < len(evt) and evt[j][0] <= T[t]:
        if evt[j][1] == 1:
            added += 1
        else:
            removed += 1
        j += 1
        
    p += added - removed
        
    dt = T[t + 1] - T[t]
    if p:
        ans += dt * mx[p - 1]
        ans2 += dt * (mx[n - 1] - (n - 1 - p) if n - 1 - p >= 0 else 0)
    
print(ans2, ans)