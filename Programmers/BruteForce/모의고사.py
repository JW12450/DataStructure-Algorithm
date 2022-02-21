def solution(answers):
    ans = []
    x = [1, 2, 3, 4, 5]
    lx = 5
    y = [2, 1, 2, 3, 2, 4, 2, 5]
    ly = 8
    z = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    lz = 10

    rx = 0
    ry = 0
    rz = 0

    for i, a in enumerate(answers):
        if x[i % lx] == a:
            rx += 1
        if y[i % ly] == a:
            ry += 1
        if z[i % lz] == a:
            rz += 1

    result = [[rx, 1], [ry, 2], [rz, 3]]

    result.sort
    # print(result)
    m = max(result)[0]
    # print(m)
    for i in range(3):
        if result[i][0] == m:
            ans.append(result[i][1])
    return ans