import sys

def up(idx):
    if idx // 2 == 0:
        return
    if heap[idx] < heap[idx // 2]:
        temp = heap[idx]
        heap[idx] = heap[idx // 2]
        heap[idx // 2] = temp
        up(idx//2)

def down(idx):
    sw = idx*2
    if sw >= len(heap):
        return
    if sw + 1 < len(heap) and heap[sw] > heap[sw+1]:
        sw += 1
    if heap[idx] > heap[sw]:
        temp = heap[idx]
        heap[idx] = heap[sw]
        heap[sw] = temp
        down(sw)

n = int(input())
heap = [0] + [int(sys.stdin.readline()) for _ in range(n)]
heap.sort()
answer = 0
while len(heap) != 2:
    
    temp = heap[1]
    heap[1] = heap[-1]
    heap[-1] = temp
    a = heap.pop()
    down(1)
    temp = heap[1]
    heap[1] = heap[-1]
    heap[-1] = temp
    b = heap.pop()
    down(1)

    sum = a + b
    answer += sum
    heap.append(sum)
    up(len(heap)-1)
    print(a, b)
print(answer)

# 10 20 30 40 50
# answer = 30
# 30 30 40 50
# answer = 90
# 40 50 90
# answer = 180
# 90 90
# answer = 270
# 180