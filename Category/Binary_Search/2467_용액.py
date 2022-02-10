import sys

n = int(sys.stdin.readline().rstrip())
"""
array = list(map(int, sys.stdin.readline().rstrip().split()))

left = 0
right = n-1
ans = (99999999999, 0, 0)
while left < right:
    sum = array[left] + array[right]
    if abs(array[left] + array[right]) < ans[0]:
        ans = (abs(sum), array[left], array[right])

    if sum > 0: # 0보다 큰 경우에는 right를 줄여줘야 함
        right -= 1
    else:  # 0보다 작은 경우에는 left를 늘려줘야 함
        left += 1

print(ans[1], ans[2])
"""
liquid = list(map(int, sys.stdin.readline().rstrip().split()))
i = 0
start = liquid[i]
n -= 1
end = liquid[n]
result = [start, end]
while start<end:

    if abs(start + liquid[n-1]) < abs(liquid[i+1] + end):
        n -= 1
        end = liquid[n]
    else:
        i += 1
        start = liquid[i]
    total = start + end
    if abs(total) < abs(sum(result)) and start < end:
        result = [start, end]
    #print(result)


print(result[0], result[1])

