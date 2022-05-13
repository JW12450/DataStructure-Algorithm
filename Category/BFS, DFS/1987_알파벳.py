#https://velog.io/@eclat12450/%EB%B0%B1%EC%A4%80-1987-%EC%95%8C%ED%8C%8C%EB%B2%B3-%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9
import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for i in range(r)]
count = [[0 for i in range(c)] for j in range(r)]

#행렬상에서 이동 기준상 하 좌 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

visited = [False]*26

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    #알파벳 리스트 만들 필요없이 킹이썬 좌표 계산 공식 외우면 개꿀이예요
    #from string import ascii_lowercase
    #alp_list = list(ascii_lowercase) 이런식으로 문제에 따라 대/소문자 리스트 빠르게 만들기도 가능~
    visited[ord( graph[x][y] ) - 65] = True
    count[x][y] += 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue

            if visited[ ord(graph[nx][ny]) - 65] :
                continue

            if not visited[ ord(graph[nx][ny]) - 65]:
                visited[ord(graph[nx][ny]) - 65] = True
                count[nx][ny] = count[x][y] + 1
                queue.append( (nx, ny))

def dfs(x, y, ans):
    global answer, visited
    answer = max(ans, answer)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        """
        한노드씩 dfs로 탐색을 하며 이때 기존의 answer보다 더 큰 ans로 탐색되는 경우의 수를 발견한 경우에는 visited 배열을 초기화(이전의 시점으로 돌아와서)하고 다시 탐색을 시작
        index 벗어나지 않는지 체크하고, 새로운 칸이 중복되는 알파벳인지 체크
        """
        if ((0 <= nx < r) and (0 <= ny < c)) and (not visited[ ord(graph[nx][ny]) - 65]):
            visited[ord(graph[nx][ny]) - 65] = True
            dfs(nx, ny, ans + 1)
            # 더 큰 ans가 탐색되서 이 코드라인으로 돌아와 실행되는 경우에 방문 초기화
            visited[ord(graph[nx][ny]) - 65] = False

answer = 1
visited[ ord(graph[0][0]) - 65] = True
dfs(0, 0, answer)
print(answer)

"""
잘못된 접근 : bfs
bfs(0,0)

for g in count:
    print(g)
    
3 6
HFDFFB
AJHGDH
DGAGEH
[1, 2, 3, 0, 0, 0]
[2, 3, 0, 0, 0, 0]
[0, 4, 0, 0, 0, 0]
"""

