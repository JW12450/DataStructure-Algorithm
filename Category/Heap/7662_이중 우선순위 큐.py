import sys, heapq

def dual_prioiry_queue(t):
    min_heap = []
    max_heap = []
    deleted = [False]*(t+1)

    for i in range(t):

        x, y = sys.stdin.readline().rstrip().split()
        y = int(y)

        if x == 'I':
            heapq.heappush(min_heap, (y, i))
            heapq.heappush(max_heap, (-y, i))

        else: #D인경우
            if y == -1: #최솟값 제외
                while len(min_heap) > 0: # min_heap에서 차례로 pop 하며 이미 지워진 애면 pop, 안지워진 애면 지우고, cnt-1
                    m = min_heap[0]
                    if deleted[m[1]] == True:
                        heapq.heappop(min_heap)
                    else:
                        heapq.heappop(min_heap)
                        deleted[m[1]] = True
                        break

            else: #최댓값 처리
                while len(max_heap) > 0:  # max_heap에서 차례로 pop 하며 이미 지워진 애면 pop, 안지워진 애면 지우고, cnt-1
                    m = max_heap[0]
                    if deleted[m[1]] == True:
                        heapq.heappop(max_heap)
                    else:
                        heapq.heappop(max_heap)
                        deleted[m[1]] = True
                        break

        #print(x, y)
        #print('min',min_heap)
        #print('max',max_heap)
        #print(deleted[:10])
        #print()

    if len(min_heap) == 0 or len(max_heap) == 0:
        print("EMPTY")
    else:
        empty = True
        while len(max_heap) > 0:  # max_heap에서 차례로 pop 하며 이미 지워진 애면 pop, 안지워진 애면 지우고, cnt-1
            m = max_heap[0]
            if deleted[m[1]] == True:
                heapq.heappop(max_heap)
            else:
                print(-m[0], end=" ")
                empty = False
                break
        while len(min_heap) > 0:  # min_heap에서 차례로 pop 하며 이미 지워진 애면 pop, 안지워진 애면 지우고, cnt-1
            m = min_heap[0]
            if deleted[m[1]] == True:
                heapq.heappop(min_heap)
            else:
                print(m[0])
                empty = False
                break

        if empty == True:
            print("EMPTY")


n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    t = int(sys.stdin.readline().rstrip())
    dual_prioiry_queue(t)


"""
def dual_prioiry_queue(t):
    heap = []
    #heap = deque()
    for _ in range(t):
        x, y = sys.stdin.readline().rstrip().split()
        y = int(y)

        if x == 'I':
            heapq.heappush(heap, y)
        else: #D인경우
            if y == -1: #최솟값 처리
                if len(heap) == 0:
                    print("",end="")
                else:
                    heapq.heappop(heap)
            else:
                if len(heap) == 0:
                    print("",end="")
                else:
                    heap.remove(heap[-1])

    if len(heap) == 0:
        return print("EMPTY")
    else:
        return print(heap[-1],heap[0])

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    t = int(sys.stdin.readline().rstrip())
    dual_prioiry_queue(t)

"""