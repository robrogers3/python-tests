def repeatedIn(s, n):
    times, remainder = divmod(n, len(s))
    return s.count('a') * times + s[:remainder].count('a')

def grep(s, t):
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

    hpow = 1
    for i in range(t_len -1):
        hpow *= K

    for i in range(t_len, s_len):
        last = s[i - t_len]
        curr = s[i]
        hash_s = (hash_s - ord(last) * hpow) * K + ord(curr)
        if hash_s == hash_t:
            #  and t == s[i - t_len + 1:i+1]:
            results.append(i - t_len + 1)

    return results
