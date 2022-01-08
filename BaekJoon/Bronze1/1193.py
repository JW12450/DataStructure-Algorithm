n = int(input())
val = n

i = 1
while True:
    n -= i
    if (n<=0):
        count = i
        break
    i +=1

#print(count)


array = []
sum = int(count*(count+1)/2)
for i in range(sum-count,sum+1):
    array.append(i)

index = int(val - (count*(count-1)/2) -1)
#print(index)

#짝수번째 대각선이면 위에서 아래로 올수록 커짐
if (count%2==0):
    print(str(index+1)+'/'+str(count-index))
#홀수번째 대각선이면 위에서 아래로 올수록 작아짐
else:
    print(str(count-index)+'/'+str(index+1))