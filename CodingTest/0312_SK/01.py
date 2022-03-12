def solution(money, costs):
    answer = 0
    costs.reverse()
    coin = [500, 100, 50, 10, 5, 1]
    pay = []
    for i in range(6):
        pay.append(costs[i] / coin[i])
    # 화폐 단위당 1원에 필요한 제작 비용 낮을수록 좋음
    while money > 0:
        min_idx = pay.index(min(pay))

        answer += money // coin[min_idx] * costs[min_idx]
        money = money % coin[min_idx]

        coin.pop(min_idx)
        costs.pop(min_idx)
        pay.pop(min_idx)

    return answer