array = list(map(int, input().split()))

d = array[0]
h = array[1]
w = array[2]

x = (h**2 + w**2) / d**2
x = x**0.5

print(int(h/x), end=" ")
print(int(w/x))