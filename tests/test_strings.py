import unittest
from helpers.strings import *

class TestStrings(unittest.TestCase):
    def test_most_common_words_in_text(self):
        s = "on the brown day the quick brown fox jumps over the brown log into the stream"
        r = most_common_words_in_text(s)
        self.assertEqual(r, 'the')

if __name__ == '__main__':
    unittest.main()
