from collections import deque


def solution(priorities, location):
    answer = 0

    queue = deque(priorities)
    cnt = 1

    while True:
        if location == 0 and queue[0] == max(queue):
            # print(cnt)
            return cnt
            break
        elif location == 0:
            save = queue.popleft()
            queue.append(save)
            location = len(queue) - 1
        elif queue[0] == max(queue):
            queue.popleft()
            cnt += 1
            location -= 1
        else:
            save = queue.popleft()
            queue.append(save)
            location -= 1
        # print(queue, location)

    return answer