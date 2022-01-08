a, b, v = map(int, input().split())

"""
# for문이 한번 루프를 돌때마다 a만큼 올라가고, b만큼 미끄러짐
while True:
    day += 1
    sum += a
    if (sum >= v):
        print(day)
        break
    sum -= b
    
이런식으로 접근하면 시간이 모자름...
"""

#정상에 도달하는 하루전날 = (최종거리 - 하루에 가는거리)를 (낮에 가는거리-밤에 미끄러지는 거리)로 나눈 몫
if (v-a) % (a-b) == 0:
    last_day_left = (v-a) // (a-b)
else:
    last_day_left = (v - a) // (a - b) + 1

if a == v:
    print(1)
elif last_day_left == 0:
    print(2)
else:
    print(last_day_left+1)



