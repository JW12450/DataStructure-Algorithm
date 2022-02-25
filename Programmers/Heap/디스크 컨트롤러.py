import heapq


def solution(jobs):
    answer = 0
    n = len(jobs)
    # 가장먼저 작업이 요청되는 시점으로 정렬후
    # 작업의 소요시간 동안 요청되는 작업들의 경우에는 작업시간이 짧은 기준으로 정렬 후 짧은애들 먼저
    heapq.heapify(jobs)
    current = heapq.heappop(jobs)
    time = current[0] + current[1]
    answer += current[1]
    while jobs:
        print(jobs)
        tmp = []
        while len(jobs) > 0 and jobs[0][0] < time:
            tmp.append(heapq.heappop(jobs))

        tmp.sort(key=lambda x: x[1])
        # print(tmp)
        while tmp:
            a = tmp.pop(0)
            answer += time + a[1] - a[0]
            time += a[1]

    return answer // n