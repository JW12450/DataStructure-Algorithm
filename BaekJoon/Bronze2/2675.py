
n = int(input())

for i in range(n):
    num, str = input().split()
    num = int(num)
    for j in range(len(str)):
        print(str[j]*num, end="")
    print()