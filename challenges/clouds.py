def jumps_count(c):
    i,jumps = 0,0
    while i < (len(c) - 1):
        if i + 2 < len(c) and c[i+2] == 0:
            i += 1
        i += 1
        jumps += 1

    return jumps
