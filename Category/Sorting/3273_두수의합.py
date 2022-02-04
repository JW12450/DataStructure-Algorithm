import sys

n = int(input())
array2 = list(map(int, input().split()))
x = int(input())

#array2 = []
#for a in array:
#    if a<=13:
#        array2.append(a)
array2.sort()

if len(array2) == 1:
    if array2[0] == x:
        print(1)
    else:
        print(0)
    sys.exit()

cnt = 0
front = 0
end = n-1
while front != end :

    if array2[front] + array2[end] == x:
        cnt += 1
        front += 1
    elif array2[front] + array2[end] > x:
        end -= 1
    else :
        front += 1

print(cnt)