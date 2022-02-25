def solution(N, number):
    answer = 0
    dp = [0] * 32001

    dp[N] = 1
    dp[N + N] = 2
    # dp[N-N] = 2
    dp[N * N] = 2
    dp[N // N] = 2
    dp[int(str(N) + str(N))] = 2

    # cnt = 2
    for cnt in range(3, 6):
        tmp = []
        for i, d in enumerate(dp):
            if d == cnt - 1:
                tmp.append(i)
        print(tmp)
        if int(str(N) * cnt) < 32001:
            dp[int(str(N) * cnt)] = cnt
        for t in tmp:
            if t + N > 0 and dp[t + N] == 0:
                dp[t + N] = cnt
            if t - N > 0 and dp[t - N] == 0:
                dp[t - N] = cnt
            if t * N < 32001 and dp[t * N] == 0:
                dp[t * N] = cnt
            if t // N > 0 and dp[t // N] == 0:
                dp[t // N] = cnt
            if t > 0 and N // t > 0 and dp[N // t] == 0:
                dp[N // t] = cnt
            # print(dp)

    if dp[number] != 0:
        answer = dp[number]
    else:
        answer = -1

    return answer