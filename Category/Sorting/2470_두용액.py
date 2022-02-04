import sys

n = int(input())
array = list(map(int, sys.stdin.readline().rstrip().split()))

#해결법 투포인터
array.sort()

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
#브루트 포스 - 메모리 초과
#print(array)
comb = list(combinations(array, 2))
#print(comb)
ans = []
for x, y in comb:
    ans.append( (abs(x+y), x, y))
ans.sort()
print(ans)
print(ans[0][1], ans[0][2])
"""

"""
#조금 더 개선된 브루트 포스 - 조금더 돌아가지만 여전히 메모리 초과

plus = [] #0 포함
minus = []
zero = False
for a in array:
    if a == 0:
        zero = True
    if a>=0:
        plus.append(a)
    else:
        minus.append(a)
if len(minus) == 0:
    plus.sort()
    print(plus[0], plus[1])
    sys.exit()
if len(plus) == 1 and zero:
    minus.sort(reverse=True)
    print(0, minus[0])
    sys.exit()

ans = []
for p in plus:
    for m in minus:
        ans.append((abs(p+m), m, p))
#print(ans)
#ans.sort()
m = min(ans)
print(m[1], m[2])
#print(ans[0][1], ans[0][2])
"""


"""
while True:
    if abs(array[left] + array[right]) > abs(array[left+1] + array[right]) or abs(array[left] + array[right]) > abs(array[left] + array[right-1]):
        if abs(array[left+1] + array[right]) < abs(array[left] + array[right-1]):
            if left+1 >= right:
                print(array[left], array[right])
                break
            left += 1
        else:
            if left >= right-1:
                print(array[left], array[right])
                break
            right -= 1
        print(array[left], array[right])
    else:
        print(array[left], array[right])
        break
"""
