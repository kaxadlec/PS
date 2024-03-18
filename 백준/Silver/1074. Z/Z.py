def divide(N, visited_cnt, pos):

    if N == 0:
        print(visited_cnt)
        return

    i, j = pos  # 기준 위치

    # 2^(N) * 2^(N)을  2^(N-1) * 2^(N-1)으로 4등분
    # 1번 정사각형   (0, 0) ~ (2^(N-1)-1, 2^(N-1)-1)
    if (i+0)<= r < (i+2**(N-1)) and (j+0)<=c<(j+2**(N-1)):
        pos = (i+0, j+0)
    # 2번 정사각형   (0, 2^(N-1)) ~ (2^(N-1)-1, 2^(N)-1)
    elif (i+0)<= r < (i+2**(N-1)) and (j+2**(N-1))<=c<(j+2**(N)):
        visited_cnt += 2**(2*N-2)
        pos = (i+0, j+2**(N-1))
    # 3번 정사각형   (2**(N-1), 0) ~ (2**(N)-1, 2**(N-1)-1)
    elif (i+2**(N-1)) <= r < (i+2**(N)) and (j+0) <= c < (j+2 ** (N - 1)):
        visited_cnt += 2**(2*N-1)
        pos = (i+2 ** (N - 1), j+0)
    # 4번 정사각형   (2^(N-1), 2^(N-1)) ~ (2^(N)-1, 2^(N)-1)
    elif (i+2**(N-1)) <= r < (i+2**(N)) and (j+2**(N-1)) <= c < (j+2**(N)):
        visited_cnt += (2**(2*N-1)+2**(2*N-2))
        pos = (i+2 ** (N - 1), j+2 ** (N - 1))

    divide(N-1, visited_cnt, pos)


N, r, c = map(int, input().split())
visited_cnt = 0
pos = (0, 0)
divide(N, visited_cnt, pos)

