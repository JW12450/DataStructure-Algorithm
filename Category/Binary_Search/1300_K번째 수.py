n = int(input())
k = int(input())

a = [[[]for i in range(n)]for j in range(n)]
for i in range(1,n+1):
    for j in range(1,n+1):
        a[i-1][j-1] = i*j

b = sum(a, [])
#for j in range(len(a)):
#    print(a[j])

#print(b)
b.sort()
#print(b)
print(b[k])