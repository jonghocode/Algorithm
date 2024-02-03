import sys

n = int(input())
chk = 0
for i in range(n):
    temp = list(map(str, sys.stdin.readline().strip().split()))
    command = temp[0]

    if command == 'add':
        num = int(temp[1])-1
        chk = chk | (1 << num)
    elif command == 'remove':
        num = int(temp[1])-1
        chk = chk & ~(1 << num)
    elif command == 'check':
        num = int(temp[1])-1
        if chk & (1 << num):
            print("출력 : 1")
        else:
            print("출력 : 0")
    elif command == 'toggle':
        num = int(temp[1])-1
        chk = chk ^ (1 << num)
    elif command == 'all':
        chk = (1 << 20) - 1
    else:
        chk = 0
