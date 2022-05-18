import sys

n, s = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

def dfs(i, sum):
    global cnt
    if i >= n:
        return
    sum += array[i]
    #합이 s가 되는 경우 cnt 추가
    if sum == s:
        cnt += 1
    #i번째 수를 더해 s가 나오지 않는 경우 해당 수를 다시 빼고 탐색
    dfs(i + 1, sum - array[i])
    # i번째 수를 더해 s가 나오지 않는 경우지만, 해당 수를 그대로 두고 탐색
    dfs(i + 1, sum)

cnt = 0
dfs(0, 0)
print(cnt)