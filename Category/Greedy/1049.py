# 끊어진 기타줄의 개수 N
# 기타줄 브랜드 M개
n, m = map(int, input().split())

# 각 브랜드의 패키지 가격(6개가 들어있는 패키지), 낱개의 가격의 input
pack = []
one = []

for i in range(m):
    a,b = map(int, input().split())
    pack.append(a)
    one.append(b)

cost = 0

min_pack = min(pack)
min_one = min(one)

#크게 3가지 경우의 수가 있음 : 다 팩으로만 사거나 팩으로 사고, 다 낱개로 사거나, 팩으로 채우고, 낱개는 1개짜리로 채우거나
cost_list = []
cost_list.append((n // 6 + 1) * min_pack)
cost_list.append(min_one * n)
cost_list.append((n // 6) * min_pack + (n % 6) * min_one)

print(min(cost_list))

"""
if min_pack < min_one: ## 6개짜리 팩이 제일 싼 하나보다도 더 싼 경우에는 그냥 넘치더라도 팩으로만 사는게 이득
    num_pack = n // 6
    cost = (num_pack + 1) * min_pack
elif min_pack/6 == min_one: #팩으로 사는 한개의 가격과 가격이 같은 경우에는 젤싼거 * 6
    cost = min_one * n
elif min_pack/6 > min_one: #팩으로 사는 한개의 가격이 하나의 가격보다 비싼 경우에는 다 개당으로 사는게 이득
    cost = min_one * n
else: ## 그외의 경우들
    if (n % 6) * min_one < min_pack: ## 나머지를 낱개로 사는 가격이 한 팩보다 더 싼경우에는 
        cost = (n // 6) * min_pack + (n % 6) * min_one
    else: ## 
        num_pack = n // 6
        cost = (num_pack + 1) * min_pack
"""


#print(cost)

"""


if min_pack < min_one or min_pack/6 < min_one:
    num_pack = n//6
    cost = (num_pack+1)*min_pack
elif min_pack/6 == min_one: #가격이 같은 경우
    num_pack = n // 6
    cost = (num_pack * min_pack) + (n%6)*min_one
elif min_pack/6 > min_one:
    cost = min_one * n
else:
    print("not find")

print(cost)
"""
