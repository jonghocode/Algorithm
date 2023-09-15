import sys
input=sys.stdin.readline
while True :
    try :
        n = int(input()) * 10000000
    except: break
    lst = []
    t = int(input())
    for i in range(t):
        lst.append(int(input()))
    lst.sort()
    answer = -987654321
    anl, anr = 0, 0
    sw = 0
    if t >= 2:
        sw = 1
    if sw == 1:
        sw2 = 0
        for i in range(len(lst)):
            if sw2==1:
                break
            l, r, k = i+1, len(lst)-1, n-lst[i]
            while l <= r:
                mid = (l + r) // 2
                if lst[mid] > k:
                    r = mid-1
                elif lst[mid] < k:
                    l = mid+1
                else:
                    if abs(lst[i] - lst[mid]) > answer:

                        answer = abs(lst[i] - lst[mid])
                        if i > mid:
                            anl, anr = mid, i
                        else:
                            anl, anr = i, mid
                        sw2 = 1
                        break
                    l = mid + 1
        if anl == 0 and anr == 0:
            print("danger")
        else:
            print("yes", lst[anl], lst[anr])
    else:
        print("danger")
