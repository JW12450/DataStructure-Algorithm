import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    # print(scoville)

    cnt = 0
    loop = 0
    while True:
        if len(scoville) == 2 and sum(scoville) < K:
            answer = -1
            break
        if scoville[0] >= K:
            answer = cnt
            break
        else:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            if a == 0 and b == 0:
                answer = -1
                break
            new = a + b * 2
            heapq.heappush(scoville, new)
            cnt += 1

    return answer