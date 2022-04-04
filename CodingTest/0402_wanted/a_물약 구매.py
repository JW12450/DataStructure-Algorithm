import sys

n = int(sys.stdin.readline())
cost = list(map(int, sys.stdin.readline().rstrip().split()))
cost.insert(0,0)

def discount(cost, dis):
    if cost-dis <=0:
        return cost-1
    else:
        return dis

array = [0]*(n+1)
discount_table = [[]for i in range(n+1)]
for i in range(1,n+1):
    t = int(sys.stdin.readline())
    for j in range(t):
        med, dis = map(int, sys.stdin.readline().split())
        array[i] += discount(cost[med-1], dis)
        discount_table[i].append((med, dis))

#array : 한 물건을 구매 후 나머지 물건들 중에서 구매했을때의 할인폭을 담고 있는 리스트
#print(array)
#print(discount_table)

def cal():
    array = [0] * (n + 1)
    for i in range(1, n+1):
        for d in discount_table[i]:
            array[i] += discount(cost[d[0]-1], d[1])

    return array
array = cal()
cnt = 0
ans = 0
visited = [False]*(n+1)
while cnt < n:
    # 해당 시점에서 가장 할인폭이 커지는 물건을 구매
    max_ = 0
    for i in range(1,n+1):
        if array[i] > max_ and not visited[i]:
            max_ = array[i]
    to_buy = array.index(max_)
    print("to_buy:",to_buy)
    ans += cost[to_buy]
    print("ans:",ans)
    cost[to_buy] = 1001
    visited[to_buy] = True
    cnt += 1

    # 구매했으므로, 가격표 갱신
    for d in discount_table[to_buy]:
        if cost[d[0]] - d[1] <=0:
            cost[d[0]] = 1
        else:
            cost[d[0]] -= d[1]
    print("cost:", cost)
    discount_table_copy = [[]for i in range(n+1)]
    for i in range(1, n+1):
        for d in discount_table[i]:
            if d[0] != to_buy:
                discount_table_copy[i].append([d[0], d[1]])
    discount_table = discount_table_copy
    print(discount_table)
    print(visited)
    array = cal()
    print("해당 인덱스의 물건을 사면 받을 수 있는 할인의 양:",array)
    print()

print(ans)


