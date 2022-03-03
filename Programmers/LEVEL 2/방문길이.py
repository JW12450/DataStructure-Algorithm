def solution(dirs):
    answer = 0
    visited = [[[[False for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(11)]
    orderlist = list(dirs)
    current = (5, 5)
    for order in orderlist:
        # print(current, answer)
        if order == 'L':
            move = (0, -1)
        if order == 'R':
            move = (0, 1)
        if order == 'U':
            move = (-1, 0)
        if order == 'D':
            move = (1, 0)
        # 범위를 벗어나는 경우는 건너 뛰기
        next = (current[0] + move[0], current[1] + move[1])
        # print( visited[current[0]] [current[1]] [next[0]] [next[1]] )

        if next[0] < 0 or next[0] > 10 or next[1] < 0 or next[1] > 10:
            continue
        else:
            if not visited[current[0]][current[1]][next[0]][next[1]]:
                # 방문 처리
                visited[current[0]][current[1]][next[0]][next[1]] = True
                visited[next[0]][next[1]][current[0]][current[1]] = True
                # 위치 갱신
                current = next
                answer += 1
            else:

                # 위치 갱신
                current = next
    return answer