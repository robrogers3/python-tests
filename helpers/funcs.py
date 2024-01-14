from structures import Utils
import random
import heapq
import arraystuff
import math
import queue
import operator
from collections import defaultdict
import collections

def fibr(n):
    if n < 2:
        return n
    return fibr(n - 1) + fibr(n - 2)

def fib_with_memo(n):
    m = {}
    def f(n):
        if n == 1 or n == 2:
            return 1
        if n in m:
            return m[n]

        r = f(n - 1) + f(n - 2)
        m[n] = r
        return r
    return f(n)

def power(x, expon):
    def pos_pow(x:int, expon:int) ->int :
        if expon == 0:
            return 1
        if expon == 1:
            return x

        half = pos_pow(x, expon//2)

        if expon % 2 == 0:
            return half * half
        else:
            return x * half * half

    if x == 0 and power <= 0:
        raise Exception('undefinded for x = 0 and negative power')

    result = pos_pow(abs(x), abs(expon))

    if expon < 0:
        return 1 / result

    if x < 0 and x % 2 == 1:
        return -result

    return result

def fib(n):
    if n < 2:
        return n

    nMinus1 = 1
    nMinus2 = 2
    nth = 1
    i = 3
    while i <= n:
        nth  = nMinus1 + nMinus2

        nMinus2 = nMinus1
        nMinus1 = nth

        i += 1

    return nth

def ways_to_climb_n_steps_top_down(n):
    a = [0 for i in range(n + 1)]
    a[0] = 1
    for i in range(1,n+1):
        one = i - 1 < 0 and 0 or a[i - 1]
        three = i - 3 < 0 and 0 or a[i - 3]
        five = i - 5 < 0 and 0 or a[i-5]
        a[i] = one + three + five

    return a[n]

def ways_to_climb_n_steps_bottom_up(n):
    a = [0 for i in range(n + 1)]
    a[0] = 1
    for i in range(n):
        if i + 1 < len(a):
            a[i + 1] += a[i]

        if i + 3 < len(a):
            a[i + 3] += a[i]

        if i + 5 < len(a):
            a[i + 5] += a[i]

    return a[n]

def ways_to_make_change(amount, coins):
    a = [0 for i in range(amount+1)]
    a[0] = 1
    for coin in coins:
        i = coin
        while i <= amount:
            a[i] = a[i] + a[i - coin]
            i += 1

    return a[amount]

def make_change(coins, amount):
    def mc(coins, target, idx, buff, summ):
        if (summ > target):
            return []
        if summ == target:
            return buff
        r = []
        for i in range(idx,len(coins)):
            buff.append(coins[i])
            t = mc(coins, target,i,buff, summ + coins[i])
            if len(t):
                r.append(t[:])
            buff.pop()

        return r

    rr = mc(coins, amount, 0, [], 0)
    return rr
    l = []
    for r in rr:
        r = arraystuff.flatten(r, 1)
        l.append(r)
    return l

def count_change(coins,amount):
    if amount == 0:
        return 1

    if amount < 0:
        return 0

    if len(coins) == 0:
        return 0

    return count_change(coins[1:], amount) + count_change(coins, amount - coins[0])

def longest_increasing_subseq(a):
    longest = [1] * len(a)
    result = 1
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] > a[j]:
                longest[i] = max(longest[i], longest[j] + 1)

        result = max(result,longest[i])

    return result

def max_diff(prices):
    min_so_far = math.inf
    max_diff = 0
    for p in prices:
        if p < min_so_far:
            min_so_far = p

        max_diff = max(p - min_so_far, max_diff)

    return max_diff

def max_diff_two_trades(prices):
    if prices is None or len(prices) < 2:
        return 0

    best_till = [0 for i in prices]
    min_so_far = math.inf
    max_diff = 0
    i = 0
    while i < len(prices):
        min_so_far = min(min_so_far, prices[i])
        max_diff = max(max_diff, prices[i] - min_so_far)
        best_till[i] = max_diff
        i += 1


    best_from = [0 for i in prices]
    max_so_far = -1
    max_diff = 0
    i = len(prices) - 1
    while i >= 0:
        max_so_far = max(max_so_far, prices[i])
        max_diff = max(max_diff, max_so_far - prices[i])
        best_from[i] = max_diff
        i -= 1

    max_two_trades = 0
    i = 0
    while i < len(prices):
        max_2nd_trade = (i + 1) < len(prices) and best_from[i+1] or 0
        max_two_trades = max(max_two_trades, best_till[i] + max_2nd_trade)
        i += 1

    return max_two_trades

def max_diff_two_trades_two(prices):
    best_from = [0 for i in prices]
    best_till = [0 for i in prices]
    max_diff = 0
    min_so_far = math.inf
    l = len(prices)
    for i in range(l):
        min_so_far = min(min_so_far, prices[i])
        max_diff = max(max_diff, prices[i] - min_so_far)
        best_till[i] = max_diff

    max_so_far = -1
    max_diff = 0
    i = len(prices) - 1
    for i in range(l - 1, -1, -1):
        max_so_far = max(max_so_far, prices[i])
        max_diff = max(max_diff, max_so_far - prices[i])
        best_from[i] = max_diff


    i = 0
    max_two_trades = 0
    for i in range(len(prices)):
        max_2nd_trade = best_from[i+1] if (i + 1) < len(prices) else 0
        max_two_trades = max(max_two_trades, best_till[i] + max_2nd_trade)


    return max_two_trades

def str_is_rotation(string, word):
    return word in string + string

def swap_array_els(a,i,j):
    a[j], a[i] = a[i], a[j]
    return a

def reverse_array_els(l, start, end):
    while start < end:
        swap_array_els(l, start, end)
        start += 1
        end -= 1

    return l
def rotate_array_by(a, n):
    n = n % len(a)
    reverse_array_els(a, 0, len(a) - 1)
    reverse_array_els(a, 0, n - 1)
    reverse_array_els(a, n, len(a) - 1)
    return a

def reverse_sentence(s):
    l = list(s)
    a = reverse_array_els(l,0, len(l) - 1)
    word_start = 0
    for i in range(len(a) -1):
        if a[i +1] == ' ':
            reverse_array_els(a, word_start, i)
            word_start = i + 2

    reverse_array_els(a, word_start, len(a) - 1)
    ss = ''.join(a)
    return ss

def rotate_90(a):
    def rotate(start, end):
        curr = 0
        while start + curr < end:
            tmp = a[start][start+curr]
            a[start][start + curr] = a[end - curr][start]
            a[end - curr][start] = a[end][end - curr]
            a[end][end - curr] = a[start+curr][end]
            a[start+curr][end] = tmp
            curr += 1


    layer = 0
    while layer < len(a)/2:
        rotate(layer, len(a) - 1 - layer)
        layer += 1

    return a
def add_two_big_nums_as_string(string1, string2):
    dec1 = "0"
    dec2 = "0"
    if string1.find('.') != -1:
        dec1 = string1[string1.find('.') +1:]
        string1 = string1[:string1.find('.')
]
    if string2.find('.') != -1:
        dec2 = string2[string2.find('.')+1:]
        string2 = string2[:string2.find('.')]

    nums1 = list(map(int, list(string1)))
    nums2 = list(map(int, list(string2)))
    maxLen = len(dec1) if len(dec1) > len(dec2) else len(dec2)
    dec1 = int(dec1.ljust(maxLen, '0'))
    dec2 = int(dec2.ljust(maxLen, '0'))
    summ = add_two_big_nums(nums1, nums2)
    print(dec1, dec2)
    dec = dec1+dec2
    if not dec:
        summ = ''.join(list(map(str, summ)))
        return summ

    dec = list(map(int, list(str(dec))))
    summ += [0] * maxLen
    total = add_two_big_nums(summ, dec)
    total = ''.join(list(map(str,total[:-maxLen]))) + '.' + ''.join(list(map(str, total[-maxLen:])))
    return total



def add_two_big_nums(a,b):
    larger = a if len(a) >= len(b) else b

    smaller = b if a == larger else a

    if len(smaller) == 0:
        return larger

    smaller = [0] * (len(larger) - len(smaller)) + smaller
    result = []
    smaller.reverse()
    larger.reverse()
    carry = 0

    for i in range(len(smaller)):
        carry,summ = divmod(larger[i] + smaller[i] + carry,10)
        result.append(summ)

    for j in range(len(smaller),len(larger)):
        carry,summ = divmod(larger[j] + carry,10)
        result.append(summ)

    if carry:
        result.append(carry)

    return result[::-1]

def add_two_big_nums_fo(a, b):
    larger = a if len(a) >= len(b) else b
    smaller = b if a == larger else a
    if len(smaller) == 0:
        return larger
    smaller = [0] * (len(larger) - len(smaller)) + smaller
    result = [0] * (len(larger) +1)
    carry = 0
    i = len(larger) - 1
    while i >= 0:
        # summ = larger[i] + smaller[i] + carry
        # carry = summ // 10
        # result[i + 1] =  summ % 10
        #print(smaller[i],i)
        carry, result[i+ 1] = divmod(larger[i] + smaller[i] + carry,10)
        i -= 1

    result[0] = carry

    if result[0] == 0:
        return result[1::]
    return result
def mul_two_big_nums(a,b):
    if not len(a) or not len(b):
        return 0
    zeros = 0
    result =  []
    i = len(a) -1
    while i >= 0:
        prod = [0] * (1 + len(b) + zeros)
        carry = 0
        j = len(b) - 1
        while j >= 0:
            carry, prod[j+1] = divmod(a[i] * b[j] + carry, 10)
            j -= 1
        prod[0] = carry
        result = add_two_big_nums(prod,result)
        zeros += 1
        i -= 1
    if result[0] == 0:
        return result[1::]
    return result
def mul_two_big_numsK(a, b):
    if a is None or b is None:
        return 0
    zeros = 0
    result = []
    i = len(a) - 1
    while i >= 0:
        prod = [0] * (1 + len(b) + zeros)
        carry = 0
        j = len(b) - 1
        while j >= 0:
            #p = a[i] * b[j] + carry
            #carry = p // 10
            #prod[j+1] = p % 10
            carry, prod[j+1] = divmod(a[i] * b[j] + carry, 10)
            j -= 1

        prod[0] = carry
        #result = prod if result is None else add_two_big_nums(result,prod)
        result = add_two_big_nums(prod,result)

        zeros += 1
        i -= 1

    if result[0] == 0:
        return result[1::]
    return result

def hash_string(s):
    x = 53
    hash = 0
    for c in s:
        hash = hash * x + ord(c)

    return hash

def str_str_three(s: str, t: str) -> list:
    if s is None or t is None:
        return []

    if len(s) < len(t):
        return []

    K = 53
    hash_t = 0
    hash_s = 0
    t_len = len(t)
    s_len = len(s)
    results = []
    for i in range(t_len):
        hash_t = hash_t * K + ord(t[i])
        hash_s = hash_s * K + ord(s[i])

    if hash_t == hash_s and t == s[0:t_len]:
        results.append(0)

    h_pow = 1
    for i in range(t_len - 1):
        h_pow *= K

    for i in range(t_len, s_len):
        last = s[i - t_len]
        curr = s[i]
        hash_s = (hash_s - ord(last) * h_pow) * K + ord(curr)
        if hash_s == hash_t and t == s[i - t_len + 1:i+1]:
            results.append(i - t_len + 1)

    return results


def str_str(s,t):
    if len(t) == 0:
        return -1
    if len(s) < len(t):
        return -1

    x = 53

    hashT = 0
    hashS = 0

    for i in range(len(t)):
        hashT = hashT * x + ord(t[i])
        hashS = hashS * x + ord(s[i])

    if hashT == hashS and t == s[0:len(t)]:
        return 0

    xPow = 1
    i = 0
    while i < len(t):
        xPow *= x
        i += 1

    i = len(t)

    while i < len(s):
        print(ord(s[i - len(t)]),s[i - len(t)])
        toRemove = ord(s[i - len(t)])
        hashS = ((hashS - toRemove * xPow) * x + ord(s[i]))
        print(hashS, toRemove, hashT)
        if t == s[i - len(t) + 1:i+1]:
            print(hashS, hashT)
            return i - len(t) + 1
        i += 1

    return -1


def update_hash(currentHash, source_string, window_size, currentIndex):
    # remove first, add ord of next
    #idx = 3 pointing 'a'
    # my new hash should based on 'oga'
    to_remove = ord(source_string[currentIndex - window_size])
    return to_remove

def hash_update(curr_hash, old_char, new_char, max_pow, K):
    return (curr_hash - ord(old_char) * max_pow) * K + ord(new_char)
def str_str_two(s: str, t: str) -> list:
    if s is None or t is None:
        return []

    if len(s) < len(t):
        return []

    K = 128
    hash_t = 0
    hash_s = 0
    t_len = len(t)
    s_len = len(s)
    results = []

    for i in range(t_len):
        hash_t = hash_t * K + ord(t[i])
        hash_s = hash_s * K + ord(s[i])

    if hash_t == hash_s and t == s[0:t_len]:
        results.append(0)

    h_pow = 1
    for i in range(t_len - 1):
        h_pow *= K

    for i in range(t_len, s_len):
        first = s[i - t_len]
        last =  s[i]
        hash_s = (hash_s - (ord(s[i-t_len]) * h_pow)) * K + ord(s[i])
        #hash_s = hash_update(hash_s, s[i-t_len], s[i], h_pow, K)

        if hash_s == hash_t and s[i-t_len+1:i+1] == t:
            # print(hash_s, hash_t)
            # print(f'hit it {s[i-t_len]+1} s[i-t_len:i] s[i-t_len+1:i+1] {s[i-t_len+1:i+1]}')
            results.append(i)

    return results


def ssearch(s: str, t: str) -> int:
    if s is None or t is None:
        return None

    if t == "":
        return 0

    s_len = len(s)
    t_len = len(t)

    if t_len > s_len:
        return None

    hash_target = 0
    hash_substring = 0
    prime = 128

    # calculate hash of target string and the first k characters of the string s (k=length of target)
    for i in range(0, t_len):
        hash_target = hash_target * prime + ord(t[i])
        hash_substring = hash_substring * prime + ord(s[i])

    # base case
    if hash_target == hash_substring and t == s[0: t_len]:
        return 0

    xPow = 1
    i = 0
    while i < len(t) - 1:
        xPow *= prime
        i += 1

    for i in range(t_len, s_len): # clever way to capture first and last characters of substring
        # this is needed since the last 2 slicing will be less than 3 characters
        first = s[i - t_len] # first character of window
        last = s[i]
        ss = s[(i-t_len)+1: i+1] # +1 is needed IMPORTANT during window slicing
        hash_substring = ((hash_substring - ord(first) * xPow)) * prime + ord(last)
        if hash_target == hash_substring and t == ss:
            return (i-t_len) + 1
    return -1 # if target is not found

def word_ladder(beginWord, endWord, wordList):
    word_set = set(wordList)
    if endWord not in word_set:
        return 0
    q = collections.deque()
    q.append([beginWord, 1])

    while q:
        word, level = q.popleft()
        if word == endWord:
            return level

        for i in range(len(word)):
            tmp = list(word)
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] != ch:
                    tmp[i] = ch
                    candidate = ''.join(tmp)
                    if candidate in word_set:
                        q.append([candidate, level + 1])
                        word_set.remove(candidate)

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

def ladder_length(beginWord, endWord, wordList):
    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return 0

    L = len(beginWord)

    all_combo_dict = defaultdict(list)
    for word in wordList:
        for i in range(L):
            all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

    # Queue for BFS
    queue = collections.deque([(beginWord, 1)])
    # Visited to make sure we don't repeat processing same word.
    visited = {beginWord: True}
    while queue:
        current_word, level = queue.popleft()
        for i in range(L):
            # Intermediate words for current word
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]

            # Next states are all the words which share the same intermediate state.
            for word in all_combo_dict[intermediate_word]:
                # If at any point if we find what we are looking for
                # i.e. the end word - we can return with the answer.
                if word == endWord:
                    return level + 1
                # Otherwise, add it to the BFS Queue. Also mark it visited
                if word not in visited:
                    visited[word] = True
                    queue.append((word, level + 1))

            all_combo_dict[intermediate_word] = []
    return 0


class Solution():
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queue for BFS
        queue = collections.deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0
def get_bit(i,num):
    return num >> i & 1

def set_bit(i, num, value):
    if value == 1:
        return (1 << i) | num

    return ~(1 << i) & num

def swap_bits(num, i, j):
    if get_bit(i,num) != get_bit(j,num):
        mask = (1 << i) | (1 << j)
        return num ^ mask

    return num

def reverse_bits(num):
    i = 0
    j = 31
    while i < j:
        num = swap_bits(num, i,j)
        i += 1
        j -= 1

    return num

def reverse_bit(num):
    result = 0
    while num:
        result = (result << 1) | (num & 1)
        num >>= 1

    return result

def count_bits(num):
    cnt = 0
    while num:
        cnt += 1
        num = num & (num -1)

    return cnt
def complement_of_num(num):
    # shift to 1 mag larger than num (+1), then - 1
    # 0101 == 5
    # 0111 wanted
    # 100 +1 <- mask
    # 1000 - 1 <-mask
    # 0111 <- mask now 7
    mask = (1 << (int(math.log(num, 2)) +1)) - 1
    #print(bin(mask),bin(num), bin(num ^ mask))
    return num ^ mask

def primes_sieve(tmax):
    sieve = [True] * (tmax + 1)
    i = 2
    while i <= math.sqrt(tmax):
        if sieve[i]:
            j = i * i
            while j <= tmax:
                sieve[j] = False
                j += i
        i += 1

    return [i for i,v in enumerate(sieve) if i > 1 and v]
    return primes
    for i in range(len(sieve)):
        if i < 2:
            continue
        if sieve[i]:
            primes.append(i)

    return primes

def similar_word_groups(words):
    def explore(w):
        visited.add(w)
        for v in edges[w]:
            if v not in visited:
                explore(v)

    res, edges, visited = 0, {}, set()
    for s in words:
        if s not in edges:
            edges[s] = set()
            for t in words:
                if t == s:
                    continue
                same = 0
                for i,c in enumerate(t):
                    if c == s[i]: same += 1
                if same == len(s) - 2:
                    edges[s].add(t)
                    if t in edges:
                        edges[t].add(s)
                    else:
                        edges[t] = {s}
    for s in words:
        if s not in visited:
            res += 1
            explore(s)

    return res
def similar_word_groups_three(words):
    def explore(s):
        visited.add(s)
        for v in edges[s]:
            if v not in visited:
                explore(v)

    res, edges, visited = 0, {}, set()
    for w in words:
        if w in edges:
            continue

        edges[w] = set()
        for t in words:
            if t == w:
                continue

            same = 0
            for i,c in enumerate(t):
                if c == w[i]: same += 1
            if same == len(w) - 2:
                edges[w].add(t)
                if t in edges:
                    edges[t].add(w)
                else:
                    edges[t] = {w}

    for w in words:
        if w not in visited:
            res += 1
            explore(w)

    return res

def similar_word_groups_two(words):
    def explore(w):
        visited.add(w)
        print(w,edges[w])
        for v in edges[w]:
            if v not in visited:
                explore(v)

    res, edges, visited = 0, {}, set()
    strs = set(words)
    for s in words:
        if s not in edges:
            edges[s] = set()
            #print('building perms for s', s)
            for i in range(len(s) - 1):
                for j in range(i+1, len(s)):
                    #print('s:i',s, 's[:i]',s[:i] , 's[j]',s[j], 's[i+1:j]', s[i+1:j], 's[i]',s[i], 's[j+1:]',s[j+1:])
                    new = s[:i] + s[j] + s[i + 1:j] + s[i] + s[j+1:]
                    #print('new ',new, len(new))
                    if new in strs:
                        edges[s].add(new)
                        if new in edges:
                            edges[new].add(s)
                        else:
                            edges[new] = {s}

    for s in words:
        if s not in visited:
            res += 1
            explore(s)

    return res

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
def base_62_encode(num):
    l = []
    while num:
        l.insert(0, chars[num % len(chars)])
        num = num // len(chars)
    return ''.join(l)
def base_62_decode(s):
    expon = 0
    num = 0
    for char in s:
        #num += chars.index(char) * (62 ** expon)
        num = num *  len(chars) + chars.index(char)
        expon += 1

    return num

def k_closest_heap(points, K):
    heap = []
    for a,b in points:
        d = a*a + b*b
        heapq.heappush(heap, (-d, a, b))
        if len(heap) > K:
            x = heapq.heappop(heap)
    return [(b,c) for a,b,c in heap]
def k_closest_sorted(points, K):
    points.sort(key = lambda p: p[0] ** 2 + p[1] ** 2)
    return points[:K]
def partion(a, start, end, pivot, pred):
    swap(a, start, pivot)
    less = start
    i = start + 1
    while i <= end:
        if pred(a[i],a[start]):
            less += 1
            swap(a, i, less)

        i += 1

    swap(a, start, less)
    return less

def select_for_target_index(a, start, end, targetIdx, pred):
    pivot = random.randint(start,end)
    result = partion(a, start, end, pivot, pred)
    if result > targetIdx:
        return select_for_target_index(a, start, result - 1, targetIdx, pred)
    elif result < targetIdx:
        return select_for_target_index(a, result + 1, end, targetIdx, pred)
    else:
        return result


def select_kth_smallest(a, k):
    pred = operator.le
    res =  select_for_target_index(a, 0, len(a) - 1, k -1,pred)
    return a[res]

def select_kth_largest(a,k):
    pred = lambda x,y: x >= y
    pred = operator.ge
    res = select_for_target_index(a,0,len(a) -1, k-1,pred)
    return a[res]

def swap(a, i,j):
    a[j], a[i] = a[i], a[j]
    return a
def sliding_window_sum(l, n):
    q = queue.Queue()
    sums = []
    summ = 0
    for i in range(len(l)):
        q.put(l[i])
        summ += l[i]
        if q.qsize() == n:
            sums.append(summ)
            item = q.get()
            summ -= item
    return sums

def calculate_the_max_price_of_a_N_day_period(prices,n):
    def add_price(price):
        while q.queue and q.queue[0][1] < (price[1] - n):
            q.get()
        q.put(price)

    q = queue.Queue()
    for price in prices:
        add_price(price)

    max = q.get()
    while q.queue:
        item = q.get()
        if item[0] > max[0]:
            max = item
    return max

def zipper(K = 2):
    def prod(val) :
        res = 1
        for ele in val:
            res *= ele
        return res

    # initialize list
    test_list = [[5, 6, 7],
                 [9, 10, 2],
                 [10, 3, 4]]

    x = zip(*test_list)
    print(list(x))
    return
    # printing original list
    print("The original list is : " + str(test_list))

    # Column Product in List of Lists
    # using loop + zip()
    res = [prod(idx) for idx in zip(*test_list)][K]

    # printing result
    print("Product of Kth column is : " + str(res))

def numToWords(num):
    teens = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
             15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}

    tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty",
            7: "seventy", 8: "eighty", 9: "ninety"}

    singles = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    results = []
    while num > 0:
        l = len(str(num))
        d = int(str(num)[0])
        if num > 99:
            results.append(singles[d])
            results.append("hundred")
        elif num > 19:
            results.append(tens[d])
        elif num > 9:
            results.append(teens[num])
            break
        else:
            results.append(singles[d])

        num %= (d * 10 ** (l-1))

    return ' '.join(results)
