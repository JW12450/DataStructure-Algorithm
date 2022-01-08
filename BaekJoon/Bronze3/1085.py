x, y ,w, h = map(int, input().split())

array = []

array.append(abs(w -x))
array.append(abs(h -y))
array.append(abs(x -0))
array.append(abs(y -0))

print(min(array))