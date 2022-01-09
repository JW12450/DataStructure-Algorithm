
#도시의 개수
num_city = int(input())
#인접한 두 도시를 연결하는 도로의 길이
lenght = list(map(int, input().split()))
#주유소의 리터당 가격
price = list(map(int, input().split()))

cost = lenght[0] * price[0]
min_price = price[0]
for i in range(1,len(lenght)):
    if (price[i] > min_price):
        cost += min_price*lenght[i]
    else:
        cost += price[i]*lenght[i]
        min_price = price[i]

print(cost)

