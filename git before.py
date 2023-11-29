#이진검색트리
import sys
sys.setrecursionlimit(10**6)

lst = []
while True:
    try :
        lst.append(int(sys.stdin.readline()))
    except:
        break

def go(temp):
    if len(temp) == 0:
        return
    left, right = [], []
    root = temp.pop(0)
    for i in range(len(temp)):
        if root < temp[i]:
            right.append(temp[i])
        elif root > temp[i]:
            left.append(temp[i])
    
    go(left)
    go(right)
    print(root)

go(lst)
print(lst[0])