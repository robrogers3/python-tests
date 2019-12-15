import heapq
from collections import OrderedDict, defaultdict, Counter

def most_common_words_in_text(str):
    d = defaultdict(lambda: 0)
    h = []
    i = 0
    common =('',0)
    for w in str.split(' '):
        d[w] += 1
        if i == 0:
            heapq.heappush(h, (-d[w], w))
            i += 1
            common  = (d[w], w)
        if d[w] > -h[0][0]:
            heapq.heapreplace(h, (-d[w], w))

        if d[w] > common[0]:
            common = (d[w], w)

    return h[0][1]
    cnt = Counter(str.split(' '))
    r = cnt.most_common(1)
    return r[0][0]
    d = defaultdict(lambda: 0)
    for w in str.split(' '):
        d[w] += 1

    od = OrderedDict(d.items(), key=lambda x: x[1])
    r = next(iter(od))
    return r
