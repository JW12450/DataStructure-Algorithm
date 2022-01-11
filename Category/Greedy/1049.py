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