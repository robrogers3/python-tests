def count(n, steps):
    if len(steps) != n:
        raise Exception('bad counting')

    map = {'U': 1, 'D': -1}
    alt = 0
    valleys = 0
    for step in steps:
        alt +=  map[step]
        if not alt and step == 'U':
           valleys += 1

    return valleys
