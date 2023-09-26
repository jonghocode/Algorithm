l, c = map(int, input().split())
lst = list(input().split())
lst.sort()

def back(mo, ja, d, idx, s):
    global l

    if d == l:
        if mo <= 0 and ja <= 0:
            print(s)
        return
    
    for i in range(idx, len(lst)):
        if lst[i] == 'a' or lst[i] == 'e' or lst[i] == 'i' or lst[i] == 'o' or lst[i] == 'u':
            back(mo-1, ja, d+1, i+1, s+lst[i])
        else:
            back(mo, ja-1, d+1, i+1, s+lst[i])


back(1, 2, 0, 0, '')