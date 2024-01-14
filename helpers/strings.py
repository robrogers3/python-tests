import heapq
from collections import OrderedDict, defaultdict, Counter, deque
import queue
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

    #return h[0][1]
    cnt = Counter(str.split(' '))
    r = cnt.most_common(1)
    return r[0][0]
    d = defaultdict(lambda: 0)
    for w in str.split(' '):
        d[w] += 1

    od = OrderedDict(d.items(), key=lambda x: x[1])
    r = next(iter(od))
    return r

def similar_word_groups(words):
    def visit(word):
        visited.add(word)
        for other in edges[word]:
            if other not in visited:
                visit(other)


    edges = {}
    visited = set()
    res = 0
    L = len(words[0])
    for word in words:
        if word in edges:
            continue
        edges[word] = set()
        for other in words:
            if word == other:
                continue
            same = 0
            for i,ch in enumerate(other):
                if word[i] == ch:
                    same += 1
            if same >= L - 2:
                edges[word].add(other)
                if other in edges:
                    edges[other].add(word)
                else:
                    edges[other] = {word}

    for word in words:
        if word not in visited:
            res += 1
            visit(word)

    return res
def word_ladder(beginWord,endWord,words):
    if endWord not in words:
        return 0
    wordSet = set(words)
    q = deque()
    q.append((beginWord, 0))
    visited = {beginWord}
    while q:
        word,level = q.popleft()
        if word == endWord:
            return level + 1

        for i in range(len(word)):
            tmp = list(word)
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] != ch:
                    tmp[i] = ch
                    candidate = ''.join(tmp)
                    if candidate in wordSet:# and candidate not in visited:
                        q.append((candidate, level + 1))
                        wordSet.remove(candidate)
                        #visited.add(candidate)

    return 0

def word_ladder_opt(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    L = len(beginWord)
    all_combo_dict = defaultdict(list)
    for word in wordList:
        for i in range(L):
            print('at',i,'combo',word[:i] + '*' + word[i+1:])
            all_combo_dict[word[:i] + '*' + word[i+1:]].append(word)

    q = deque()
    q.append((beginWord, 0))
    visited = {beginWord:True}
    while q:
        current_word, level = q.popleft()
        if current_word == endWord:
            return level + 1

        for i in range(L):
            intermediate_word = current_word[:i] + '*' + current_word[i+1:]
            for word in all_combo_dict[intermediate_word]:
                if word == endWord:
                    print('found',current_word, word)
                    return level + 1
                if word not in visited:
                    visited[word] = True
                    q.append((word, level + 1))

    return 0
import heapq
from collections import OrderedDict, defaultdict, Counter, deque

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

    #return h[0][1]
    cnt = Counter(str.split(' '))
    r = cnt.most_common(1)
    return r[0][0]
    d = defaultdict(lambda: 0)
    for w in str.split(' '):
        d[w] += 1

    od = OrderedDict(d.items(), key=lambda x: x[1])
    r = next(iter(od))
    return r

def similar_word_groups(words):
    def visit(word):
        visited.add(word)
        for other in edges[word]:
            if other not in visited:
                visit(other)


    edges = {}
    visited = set()
    res = 0
    L = len(words[0])
    for word in words:
        if word in edges:
            continue
        edges[word] = set()
        for other in words:
            if word == other:
                continue
            same = 0
            for i,ch in enumerate(other):
                if word[i] == ch:
                    same += 1
            if same >= L - 2:
                edges[word].add(other)
                if other in edges:
                    edges[other].add(word)
                else:
                    edges[other] = {word}

    for word in words:
        if word not in visited:
            res += 1
            visit(word)

    return res
def word_ladder(beginWord,endWord,words):
    if endWord not in words:
        return 0
    wordSet = set(words)
    q = deque()
    q.append((beginWord, 0))
    visited = {beginWord}
    while q:
        word,level = q.popleft()
        if word == endWord:
            return level + 1

        for i in range(len(word)):
            tmp = list(word)
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] != ch:
                    tmp[i] = ch
                    candidate = ''.join(tmp)
                    if candidate in wordSet:# and candidate not in visited:
                        q.append((candidate, level + 1))
                        wordSet.remove(candidate)
                        #visited.add(candidate)

    return 0

def word_ladder_opt(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    L = len(beginWord)
    all_combo_dict = defaultdict(list)
    for word in wordList:
        for i in range(L):
            all_combo_dict[word[:i] + '*' + word[i+1:]].append(word)

    q = deque()
    q.append((beginWord, 0))
    visited = {beginWord:True}
    while q:
        current_word, level = q.popleft()
        if current_word == endWord:
            return level + 1

        for i in range(L):
            intermediate_word = current_word[:i] + '*' + current_word[i+1:]
            for word in all_combo_dict[intermediate_word]:
                if word not in visited:
                    visited[word] = True
                    q.append((word, level + 1))
    return 0

def ll(beginWord,endWord, wordList):
    L = len(beginWord)
    all_combo_dict = defaultdict(list)
    for word in wordList:
        for i in range(L):
            all_combo_dict[word[:i] + '*' + word[i+1:]].append(word)

    q = queue.Queue()
    q.put((beginWord, 1))
    visited = {beginWord: True}
    while q:
        current_word, level = q.get()
        for i in range(L):
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]
            for word in all_combo_dict[intermediate_word]:
                if word == endWord:
                    return level + 1

                if word not in visited:
                    visited[word] = True
                    q.put((word, level+1))

            all_combo_dict[intermediate_word] = []
    return 0
