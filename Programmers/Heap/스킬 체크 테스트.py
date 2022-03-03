import heapq


def solution(A, B):
    answer = 0
    A.sort(reverse=True)

    # B팀에선 A를 이길수 있는 애들중에 제일 작은 애를 내는게 이득임..!
    B = [-b for b in B]
    heapq.heapify(B)

    for a in A:
        # B에서 제일 큰 애가 a보다 작은경우엔 더 이상 이길일이 없으므로 종료
        if -B[0] <= a:
            B.pop()
        else:
            save = []
            end = True
            # 맥스 힙에서 꺼낸 값이 상대할 A보다 작을때까지 쭉 꺼내서 save에 저장한뒤, save에서 제일 작은애를 내보냄.
            while B:
                m = heapq.heappop(B) * (-1)
                # 더 작은 애가 나오면, 다시 B에 넣어줌
                if m < a:
                    break
                else:
                    save.append(-m)

            heapq.heappush(B, -m)
            answer += 1
            save.pop()
            for s in save:
                heapq.heappush(B, s)

    return answer