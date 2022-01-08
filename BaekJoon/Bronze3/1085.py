x, y ,w, h = map(int, input().split())

array = []

array.append(abs(w -x))
array.append(abs(h -y))

print(min(array))