weight = int(input())

# 전체 시도해볼 조합의 횟수 : 숫자가 큰 5로 나눈 몫의 크기만큼
try_num = weight//5

can = []
ans = []

for i in range(try_num+1):
    weight_try = weight - (5*i)
    if (weight_try % 3 == 0):
        ans.append(i+(weight_try/3))

if (len(ans) == 0):
    print(-1)
else:
    print(int(min(ans)))