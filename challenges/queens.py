
def attack(n,k,r_q,c_q, obs):
    def moves(updated_row, updated_col, r, c, obstacles):
        cnt = 0
        while True:
            r = updated_row(r)
            c = updated_col(c)
            key =  f'{r},{c}'
            if (c < 1 or c > n or r < 1 or r > n) or (key in obstacles):
                break

            cnt += 1

        return cnt

    obstacles = {}
    for o in obs:
        obstacles[f'{o[0]},{o[1]}'] = None

    dr = [-1,-1,-1, 0, 0, 1, 1, 1]
    dc = [ 0,-1, 1, 1,-1, 0, 1,-1]
    cnt = 0
    for i in range(8):
        cnt += moves(lambda r: r + dr[i], lambda c: c + dc[i], r_q, c_q, obstacles)

    return cnt
