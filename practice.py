from heapq import heappush, heappop
import sys

n = int(input())
promax = [] # 최대힙
promin = [] # 최소힙
sol = {}
lst = {}
for _ in range(n):
    p, l = map(int, sys.stdin.readline().split())
    heappush(promax, [-l, -p])
    heappush(promin, [l, p])
    lst[str(p)] = str(l)

m = int(input())
for _ in range(m):
    command = list(sys.stdin.readline().strip().split())
    if command[0] == 'add': # 더하기
        lst[str(command[1])] = str(command[2])
        heappush(promax, [-int(command[2]), -int(command[1])])
        heappush(promin, [int(command[2]), int(command[1])])

    elif command[0] == 'recommend': # 추천하기
        if command[1] == '1':
            while True: # sol안에 없는 것을 뽑을 때 까지 뽑기
                level, pro = -promax[0][0], -promax[0][1]
                level = str(level)
                pro = str(pro)
                if pro in sol:
                    if level in sol[pro]:
                        heappop(promax)
                    else:
                        print(pro)
                        break
                else:
                    print(pro)
                    break
        
        
        elif command[1] == '-1':
            while True: # sol안에 없는 것을 뽑을 때 까지 뽑기
                level, pro = promin[0][0], promin[0][1]
                level = str(level)
                pro = str(pro)
                if pro in sol:
                    if level in sol[pro]:
                        heappop(promin)
                    else:
                        print(pro)
                        break
                else:
                    print(pro)
                    break

    elif command[0] == 'solved': # 풀었으면 sol에 넣기
        if command[1] not in sol:
            sol[command[1]] = []
        sol[command[1]].append(lst[command[1]])
        
    # print(f"promin : {promin}, solved : {sol}")