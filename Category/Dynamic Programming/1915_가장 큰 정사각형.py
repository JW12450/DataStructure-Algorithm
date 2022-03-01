import sys
from collections import deque


def getMaxField(data, n, m):
    '''
    n개의 줄에 m개의 숫자가 차례로 주어질 때, 가장 큰 잡초밭을 출력하는 함수를 작성하세요.
    '''
    ans = []
    for i in range(n):
        for j in range(m):
            square = True
            if data[i][j] == 0:
                continue
            else:
                width = 0
                while j + width < n and i + width < m and data[i][j + width]:
                    width += 1
                for x in range(i, i + width):
                    for y in range(j, j + width):
                        if data[x][y] != 1:
                            square = False
                if square:
                    ans.append(width * width)
                # print(ans)

    return ans


def main():
    '''
    이 부분은 수정하지 마세요.
    '''
    inputList = [int(x) for x in input().split()]

    n = inputList[0]
    m = inputList[1]
    #data = [[int(x) for x in input().split()] for i in range(n)]
    data = [list(map(int, list(input()))) for i in range(n)]
    for d in data:
        print(d)
    print(max(getMaxField(data, n, m)))


if __name__ == "__main__":
    main()

