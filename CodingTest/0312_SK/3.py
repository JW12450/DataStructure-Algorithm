import math

def solution(width, height, diagonals):
    #대각선이 있는 좌표를 기준으로 해당 대각선을 한번만 이용하므로 대각선의 리스트에서 한 대각선을 이용하는 경우만 고려
    #하나의 대각선을 이용하는 경우
    #해당 선의 (원점에서 왼쪽위 꼭지점까지의 최단거리 경우의수) * (오른쪽 아래 꼭지점에서 목표까지의 최단거리 경우의수 )
    #+
    #해당 선의 (원점에서 오른쪽 아래 꼭지점까지의 최단거리 경우의 수) * (왼쪽 위 꼭지점에서 목표까지의 최단거리 경우의 수)
    #를 더한걸 각각의 대각선별로 수행
    answer = 0
    mf = math.factorial
    for d in diagonals:
        cnt = 0
        x, y = d[0], d[1]

        cnt += ((mf(x + y-1)/(mf(x)*mf(y-1))) * (mf(width-x+1 + height-y)) / (mf(width-x+1) * mf(height-y)))%10000019
        cnt += ((mf(x-1 + y)/(mf(x-1)*mf(y))) * (mf(width-x + height-y+1) / (mf(width-x) * mf(height-y+1))))%10000019
        answer += cnt
    return answer