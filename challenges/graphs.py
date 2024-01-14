import collections
def allpathsSourceToTarget1(graph, start, target):
    result = []
    queue = collections.deque(start)
    while queue:
        path = queue.popleft()
        print('pop', path, path[-1])

        if path[-1] == len(graph) -1:
            print('appending',path)
            print('at end target is ', target, path[-1])
            result.append(path)
        else:
            for next_node in graph[path[-1]]:
                print('append queue', next_node)
                queue.append(path + [next_node])

    return result

def allPathsSourceToTarget2(g, s,e):
    result = []
    q = collections.deque([s])
    p = collections.defaultdict(set)
    while q:
        v = q.popleft()
        for n in g.get(v, []):
            print(n)
            p[n].add(v)
            q.append(n)

    return p

def ap2(g, start, end):
    result = []
    q = collections.deque([[start]])
    i = 0
    while q:
        path = q.popleft()
        neighbors = g.get(path[-1], [])
        for node in neighbors:
            if node == end:
                result.append(path[:] + [e])
            else:
                q.append(path + [node])

    return ['->'.join(r) for r in  result]

def find_all_parents(G, s):
    Q = [s]
    parents = collections.defaultdict(set)
    while len(Q) != 0:
        v = Q[0]
        Q.pop(0)
        for w in G.get(v, []):
            parents[w].add(v)
            Q.append(w)
    return parents

def find_all_paths(parents, a, b):
    results = []
    if a == b:
        return [a]
    else:
        for x in list(parents[b]):
#            print(b,x)
            for p in find_all_paths(parents, a, x):
                results.append(p+'->'+b)
    return results
    return [a] if a == b else [y + b for x in list(parents[b]) for y in find_all_paths(parents, a, x)]

def all_paths(g, s, e):
    return find_all_paths(find_all_parents(g,s), s, e)
