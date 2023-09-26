cnt = 1
while True:
    x, y, z = map(int, input().split())
    if not(x+y+z): break
    if z%y > x:
        print(f'case {cnt}: {z//y*x+x}')
    else:
        print(f'case {cnt}: {z//y*x + z%y}')
    cnt+=1
