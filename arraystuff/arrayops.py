import queue
import heapq
import operator
import random
from itertools import chain
from queues.QueueWithMax import QueueWithMax
from heaps import MaxHeap, MinHeap

def calculate_max_of_sliding_windows(l, n):
    q = QueueWithMax()
    r = []
    deque = False
    for k,v in enumerate(l):
        q.enqueue(v)
        if deque:
            q.deque()
            r.append(q.findMax())

        if k + 1 == n:
            deque = True
            r.append(q.findMax())

    return r

def calculate_the_max_price_of_a_N_day_period(prices,n):
    q = queue.PriorityQueue()
    def add_price(price):
        while not q.empty() and q.queue[0][1] < (price[1] - n):
            q.get(False)

        price[0] = -price[0]
        q.put(price)

    for price in prices:
        add_price(price)

    item =  q.get()
    item[0] = -item[0]

    return item

    max = q.get(False)
    while not q.empty():
        item = q.get()
        if item[0] > max[0]:
            max = item

    return max


def calculate_sliding_windows_sums(l, k):
    q = queue.Queue()
    sums = []
    sum = 0
    for i in range(len(l)):
        if q.qsize() == k:
           sums.append(sum)
           item = q.get()
           sum -= item

        q.put(l[i])
        sum += l[i]

    sums.append(sum)
    return sums

def reverse_list(alist):
    N = len(alist)
    for i in range(N//2):
        alist[i], alist[N - i - 1] = alist[N - i - 1], alist[i]
    return alist

def sort_squares_list(a):
    if len(a) == 0:
        return []

    s = 0
    e = len(a) - 1
    r = [None] * len(a)
    ridx = len(r) - 1

    while(s <= e):
        if abs(a[s]) > abs(a[e]):
            r[ridx] = pow(a[s],2)
            s += 1
        else:
            r[ridx] = pow(a[e],2)
            e -= 1

        ridx -= 1

    return r

def sub_array_equal_to_sum(l, t):
    if len(l) == 0:
        return []
    sum = l[0]
    s = 0
    e = 0
    a = []
    while(s <= len(l)):
        if (s > e):
            e = s
            sum = a[s]

        if sum < t:
            if (e == len(l) - 1):
                break

            e += 1
            sum += l[e]

        elif sum > t:
            sum -= l[s]
            s += 1

        else:
            return l[s:e+1]

    return []
def max_sum_of_sub_array(l):
    if len(l) == 0:
        raise Exception("input list is empty")

    maxEndingHere = l[0]
    maxV = maxEndingHere
    for v in l[1:]:
        maxEndingHere = max(v, maxEndingHere + v)
        maxV = max(maxV, maxEndingHere)

    return maxV

def partion_using_pivot(l, p):
    if len(l) <= 1:
        return l

    lb = 0
    hb = len(l) - 1
    i = 0
    while(i <= hb):
        if l[i] < p:
            l[lb], l[i] = l[i], l[lb]
            lb += 1
            i += 1
        elif l[i] > p:
            l[hb], l[i] = l[i], l[hb]
            hb -= 1
        else:
            i += 1

    return l


def move_zeros_to_start(l):
    if len(l) <= 1:
        return l

    b = 0
    for i, v in enumerate(l):
        if v == 0:
            l[b], l[i] = l[i], l[b]
            b += 1

    return l

def move_zeros_to_end(l):
    if len(l) <= 1:
        return l

    i = len(l) - 1
    b = i
    while(i >= 0):
        if l[i] == 0:
            l[b], l[i] = l[i], l[b]
            b -= 1
        i -= 1

    return l

def slice_to_target(a, t):
    if len(a) == 0:
        return []
    l = len(a)
    s = 0;
    e = 0
    sum = a[0]
    while s < l:
        if (s > e):
            e = s
            sum = a[s]

        if sum < t:
            e += 1
            if e == l:
                break

            sum += a[e]

        elif sum > t:
            sum -= a[s]
            s +=1

        elif sum == t:
            return [s,e]

    return []

def find_k_largest(a,k):
    h = MinHeap()
    for i in range(len(a)):
        if i < k:
            h.push(a[i])
        elif a[i] > h.peek():
            h.pop()
            h.push(a[i])

    return h.getItems()

def find_k_smallest(a, k):
    h = MaxHeap()
    for i in range(len(a)):
        if i < k:
            h.push(a[i])
        elif a[i] < h.peek():
            popped = h.pop()
            h.push(a[i])

    return h.getItems()
    h = []
    heapq.heapify(h)

    for i in range(len(a)):
        if i < k:
            heapq.heappush(h, -a[i])
        elif a[i] < -h[0]:
            heapq.heapreplace(h, -a[i])

    return [-i for i in h]

def gen_combos(l, n):
    def combos(l, b, lidx, bidx):
        if bidx == len(b):
            return b

        if lidx == len(l):
            return None

        r = []
        for i in range(lidx,len(l)):
            b[bidx] = l[i]
            c = combos(l,b,i+1,bidx+1)
            if c and len(c):
                r.append(c[:])

        return r

    if n > len(l):
        return []

    b = [None] * n
    return combos(l, b, 0, 0)

def gen_perms(l, n):
    def perms(a, b, bidx, inb):
        if bidx == len(b):
            return b

        r = []
        for i in range(len(a)):
            if inb[i] == False:
                b[bidx] = a[i]
                inb[i] = True
                p = perms(a,b,bidx+1, inb)
                r.append(p[:])
                inb[i] = False

        return r

    b = [None] * n
    inb = [False] * len(l)
    return flatten(perms(l, b, 0, inb))

def flatten(l, depth = 1):
    def f(l, a, depth):
        for i in l:
            if depth > 0 and isinstance(i, list):
                f(i, a, depth -1)
            else:
                a.append(i)

        return a
    return f(l, [], depth)

def gen_phone_number_words(num):
    letterMap = {
        0: (),
        1: (),
        2: ('a','b','c'),
        3: ('d','e','f'),
        4: ('g','h','i'),
        5: ('j','k','l'),
        6: ('m','n','o'),
        7: ('p','q','r','s'),
        8: ('t','u','v'),
        9: ('w','x','y','z')
    }

    def gen(a,b,aidx, bidx):
        if bidx == len(b) or aidx == len(a):
            return b

        letters = letterMap[int(a[aidx])]

        if len(letters) == 0:
            return gen(a,b,aidx+1,bidx)

        r = []
        for letter in letters:
            b[bidx] = letter
            t = gen(a,b,aidx+1,bidx+1)[:]
            if t:
                r.append(t)

        return r

    x = list(map(int, str(num)))
    return flatten(gen(x, [-1] * len(x), 0,0),len(x) - 1)

def subsets(a):
    if len(a) == 0:
        return []

    all = []
    sets = subsets(a[1:])
    for s in sets:
        all.append(flatten([a[0], s]))
    else:
        all.append(a[0])

    all.extend(sets)
    return all

def zig_zag_collect(m):
    row, col = 0, 0
    up = True
    res = []
    while True:
        res.append(m[row][col])
        if (row == 0 or row == len(m) - 1) and col != len(m[0]) - 1:
            col += 1
            res.append(m[row][col])
            up = not up
        elif col == 0 or col == len(m[0]) - 1:
            row += 1
            res.append(m[row][col])
            up = not up

        if row == len(m) - 1 and col == len(m) - 1:
            return res

        row += -1 if up else  1
        col +=  1 if up else -1

    return []

def spiral_collect(a):
    def collect_layer(layer, lastCol, lastRow):
        if lastCol == layer or lastRow == layer:
            res.append(a[layer][layer])

        #top row
        curr = layer
        while curr < lastCol:
            res.append(a[layer][curr])
            curr += 1

        #right col
        curr = layer
        while curr < lastRow:
            res.append(a[curr][lastCol])
            curr += 1

        # bottom row
        curr = lastCol
        while curr > layer:
            res.append(a[lastRow][curr])
            curr -= 1

        # left col
        curr = lastRow
        while curr > layer:
            res.append(a[curr][layer])
            curr -= 1

    res = []
    if len(a) == 0:
        return res

    #eg. 5 rows, 5 cols
    # layer = 0: top = 0, right = 4, bottom = 4, left = 0
    # layer = 1, top = 1, right = 3, bottom = 3, left = 1
    # layer = 2, top = 2, right = 2, bottom = 2, left = 2 <-- single middle element
    layer = 0
    while layer <= len(a) // 2:
        collect_layer(layer=layer, lastCol=len(a[0]) - 1 - layer, lastRow=len(a) - 1 - layer)
        layer += 1


    return res

def rotate_ninty_clockwise(a):
    #it's a sq,
    N = len(a[0])
    i = 0
    m = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            # temp= a[i][j]
            # a[i][j] = a[N - 1 - j][i]
            # a[N - 1 - j][i] = a[N - 1 - i][N - 1 - j]
            # a[N - 1 - i][N - 1 - j] = a[j][N - 1 - i]
            # a[j][N - 1 - i] = temp
            # continue
            tl = a[i][j]
            tr = a[j][N - 1 - i]
            bl = a[N - 1 - j][i]
            br = a[N - 1 - i][N - 1 - j]

            # print(i,j)
            # print('top left',tl,(i,j))
            # print('top right',tr, (j, N - 1 -i))
            # print('bttow right', br, (N - 1 - i, N - 1 - j))
            # print('bottow left', bl, (N - 1 - j, i))

            # top left set to bottom left
            a[i][j] = bl
            # top right set to top left
            a[j][N - 1 - i] = tl

            # bottom left set to bottom right
            a[N-1-j][i] = br
            # bottom right set to top right
            a[N - 1 -i][N - 1 -j] = tr

    return a
def rotate_ninty(arr):
    def rotate(a,start, end):
        curr = 0
        while start + curr < end:
            #print('rotate',curr, start,curr + start, end)
            # save top left e.g. a[0][0] -> int(1)
            tmp = a[start][start+curr]
            # set top left to val of bottom left
            # e.g. a[0][0+0] = a[2 - 0][0]
            a[start][start + curr] = a[end - curr][start]
            # set bottom left to val of bottom right
            # e.g. a[2 - 0][0] = a[2][2 - 0]
            a[end - curr][start] = a[end][end - curr]
            # set bottom right to val of top right
            # e.g. a[2][2 - 0] = a[0 + 0][2]
            a[end][end - curr] = a[start+curr][end]
            # set top right, e.g. a[0][2] to tmp i.e. top left
            # e.g. a[0+0][2] = tmp = a[start][start + curr]
            a[start+curr][end] = tmp
            curr += 1

    layer = 0
    while layer < (len(arr) // 2):
        rotate(arr,layer, len(arr) - 1 - layer)
        layer += 1

    return arr

def swap(a, i,j):
    a[j],a[i] = a[i],a[j]

def reverse_array_els(a, start, end):
    while start < end:
        swap(a,start,end)
        start += 1
        end -= 1
def reverse_columns(arr):
    C = len(arr)
    for i in range(C):
        j = 0
        k = C-1
        while j < k:
            t = arr[j][i]
            arr[j][i],arr[k][i] = arr[k][i],arr[j][i]
            #arr[k][i] = t
            j += 1
            k -= 1

    return arr

def reverse_array(a):
    reverse_array_els(a, 0, len(a) -1)


def transpose(a):
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]

def find_missing_num(a, n):
    expected =  n*(n+1)/2
    return expected - sum(a)

def find_single_number(a):
    result = 0
    for el in a:
        result ^= el
    return result

def partion(a, start, end, pivot, pred):
    swap(a,start,pivot)
    less = start
    for i in range(start+1,end+1):
        if pred(a[i], a[start]):
            less += 1
            swap(a,i,less)

    swap(a, start, less)
    return less

def select_for_target_index(a, start, end, targetIdx, pred):
    pivot = random.randint(start, end)
    result = partion(a, start, end, pivot, pred)
    if result == targetIdx:
        return result
    if result > targetIdx:
        return select_for_target_index(a, start, result -1, targetIdx, pred)

    #result < targetIdx
    return select_for_target_index(a, result +1, end, targetIdx, pred)

def select_kth_largest(a,k):
    pred = operator.ge
    res = select_for_target_index(a, 0, len(a) - 1, k - 1, pred)
    return a[res]

def select_kth_smallest(a, k):
    pred = operator.le
    res = select_for_target_index(a, 0, len(a) - 1, k - 1, pred)
    return a[res]

def merge_sub_arrays(a, start, mid, end):
    res = [None] * (end - start + 1)
    i = start
    j = mid + 1
    resPos = 0

    while i <= mid and j <= end:
        if a[i] < a[j]:
            res[resPos] = a[i]
            i += 1
        else:
            res[resPos] = a[j]
            j += 1

        resPos += 1

    while i <= mid:
        res[resPos] = a[i]
        resPos += 1
        i += 1

    while j <= end:
        res[resPos] = a[j]
        resPos += 1
        j += 1


    for k in range(len(res)):
        a[start+k] = res[k]

def merge_sort(a):
    def msort(a, start, end):
        if start >= end:
            return

        mid = start + ((end - start) >> 1)

        msort(a, start, mid)
        msort(a, mid + 1, end)
        merge_sub_arrays(a, start,mid,end)

    if not len(a): return a
    msort(a, 0, len(a) - 1)
    return a

def dutch_national_flag(a, start, end, pivotIdx):
    pivot = a[pivotIdx]
    low = start - 1
    mid = start - 1
    high = end + 1
    while mid + 1 < high:
        if a[mid+1] > pivot:
            swap(a, high-1, mid+1)
            high -= 1
        elif a[mid+1] == pivot:
            mid +=1
        else:
            swap(a,mid+1,low+1)
            mid += 1
            low += 1

    return [low,high]

def quick_sort(a):
    def qsort(a, start, end):
        if start < 0 or end >= len(a) or start >= end:
            return

        pivotIdx = random.randint(start,end)
        points = dutch_national_flag(a, start,end,pivotIdx)
        qsort(a, start, points[0])
        qsort(a,points[1], end)


    if not a or not len(a):
        return a

    qsort(a,0,len(a) - 1)
    return a

def bucket_sort(a):
    buckets = [None] * len(a)
    for el in a:
        buckets[el] = el

    return buckets

def sort_lists(m):
    result = []
    q = queue.PriorityQueue()
    for v in chain(*m):
        q.put(v)

    while q.qsize():
        result.append(q.get())

    return result

def length(arr):
    def l(i, a, p):
        if i < len(a):
            p += 1
            i +=1
            return l(i,a,p)
        else:
            return p

    p = l(0,arr, 0)

    return p

def dnf(a, idx):
    pivot = a[idx]
    low = -1
    mid = -1
    high = len(a)
    while mid + 1 < high:
        if a[mid+1] > pivot:
            swap(a, high -1, mid + 1)
            high -= 1
        elif a[mid+1] == pivot:
            mid +=1
        else:
            swap(a, mid +1, low+1)
            mid += 1
            low += 1

    return a
