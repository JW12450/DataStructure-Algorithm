bridge_length = 2
weight = 100
truck_weights = [7, 4, 5, 6]
road = []
b_weight = []
time = 0
while True:
    print(b_weight)
    if len(truck_weights) > 0 and sum(b_weight) + truck_weights[0] < weight and len(road) <= bridge_length:
        # 다음 트럭도 출발시킬수 있는 상황
        t = truck_weights.pop(0)
        b_weight.append(t)
        road.append(0)
        for i in range(len(road)):
            road[i] += 1
        # 다리를 다 건너간 트럭이 있으면 제거
        if road[0] == bridge_length:
            road.pop(0)
            b_weight.pop(0)
        print(b_weight)
        # 모든 트럭이 다리를 다 건넌경우
        if len(truck_weights) == 0 and len(road) == 0:
            break

        time += 1
    else:
        # 다음 트럭이 다리에 올라서면 출발이 불가능한 경우
        for i in range(len(road)):
            road[i] += 1

        # 다리를 다 건너간 트럭이 있으면 제거
        if road[0] == bridge_length:
            road.pop(0)
            b_weight.pop(0)

        # 모든 트럭이 다리를 다 건넌경우
        if len(truck_weights) == 0 and len(road) == 0:
            break

        time += 1


print(time)