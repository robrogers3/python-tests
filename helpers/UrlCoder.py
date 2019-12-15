import string
import random
from collections import OrderedDict


class UrlCoder:
    def __init__(self):
        self.urls = []
        self.base = OrderedDict((k, i) for i, k in enumerate(string.digits + string.ascii_letters))

    def encode(self, longUrl):
        self.urls.append(longUrl)
        n = len(self.urls)
        keys = list(self.base.keys())
        code = []
        while n > 0:
            code.append(keys[n % len(self.base)])
            n = n // len(self.base)

        return 'http://tinyurl.com/' + ''.join(code)

    def decode(self, shortUrl):
        code = shortUrl.split('/')[-1]
        n = 0
        expon = 0
        for ch in code:
            print(self.base[ch], ch, len(self.base))
            #n = n * len(self.base) + self.base[ch]
            n += self.base[ch] * (62 ** expon)
            expon += 1

        return self.urls[n-1]

class UrlCoderX:
    def __init__(self):
        self.base = OrderedDict((k, i) for i, k in enumerate(string.digits + string.ascii_letters))
        self.urls = ['http://google.com/' + str(i) for i in range(1,20000)]

    def encode(self, longUrl):
        self.urls.append(longUrl)
        keys = list(self.base.keys())
        code = []
        n = len(self.urls)
        print('len n', n)
        while n > 0:
            code.append(keys[n % len(self.base)])
            n = n // len(self.base)

        return 'http://tinyurl.com/' + ''.join(code)

    def decode(self, shortUrl):
        code = shortUrl.split('/')[-1]
        n = 0
        for ch in code:
            n = n * len(self.base) + self.base[ch]

        print('decode',n)
        #return self.urls[n - 1]
