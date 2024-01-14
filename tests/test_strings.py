import unittest
from helpers.strings import *

class TestStrings(unittest.TestCase):
    def test_most_common_words_in_text(self):
        s = "on the brown day the quick brown fox jumps over the brown log into the stream"
        r = most_common_words_in_text(s)
        self.assertEqual(r, 'the')

    def test_similar_word_groups(self):
        w = ["star","tars","rats","arts"]
        r = similar_word_groups(w)
        self.assertEqual(2,r)
        w = ["star","tars","rats","arts","frat", "traf", "tarf","carf"]
        r = similar_word_groups(w)
        self.assertEqual(r,3)

    def test_word_ladder(self):
        word_set = {'hot', 'dot','dog', 'lot','log', 'cog'}
        start = 'hit'
        end = 'cog'
        r = word_ladder(start,end,list(word_set))
        self.assertEqual(5,r)

    def test_word_ladder_opt(self):
        word_set = {'hot', 'dot','dog', 'lot','log', 'cog'}
        start = 'hit'
        end = 'cog'
        r = word_ladder_opt(start,end,list(word_set))
        print('opt',r)
        r = ll(start,end,list(word_set))
        self.assertEqual(5,r)

if __name__ == '__main__':
    unittest.main()
