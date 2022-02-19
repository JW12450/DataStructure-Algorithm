n,l = map(int, input().split())

water = list(map(int, input().split()))
water.sort()


cnt = 1
start = water[0]
end = start + l

for i in range(n):
    if start <= water[i] < end:
        continue
    else:
        start = water[i]
        end = water[i] + l
        cnt += 1

print(cnt)



