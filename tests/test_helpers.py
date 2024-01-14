import unittest
from helpers import *

class TestHelpers(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(34, fibr(9))

    def test_fib_memo(self):
        self.assertEqual(34, fib_with_memo(9))

    def test_power(self):
        self.assertEqual(power(2,32),pow(2,32))

    def test_it_can_calculate_ways_to_climb_bottom_up(self):
        r = ways_to_climb_n_steps_bottom_up(8)
        self.assertEqual(19,r)

    def test_it_can_calculate_ways_to_climb_top_down(self):
        r = ways_to_climb_n_steps_bottom_up(8)
        self.assertEqual(19,r)

    def test_it_can_make_change(self):
        r = ways_to_make_change(5, [5,1,2])
        self.assertEqual(4, r)

    def test_count_change(self):
        r = count_change([5,1,2],5)
        self.assertEqual(4, r)

    def test_longest_increasing_subseq(self):
        l =  [7, 1, 3, 2, 5, 3, 5,6]
        e = [1, 2, 3, 5, 6]
        r = longest_increasing_subseq(l)
        self.assertEqual(len(e), r)

    def test_calculates_max_diff(self):
        l = [9,3,2,1,5,7,2,8,3,4] #[9,3,2,​1​,5,7,2,​8​,3,4]
        e = 7
        r = max_diff(l)
        self.assertEqual(e,r)

    def test_string_is_rotation(self):
        string = 'atbobc'
        word = 'bobcat'
        r = str_is_rotation(string, word)
        self.assertEqual(True, r)

    def test_calculates_max_diff_two_trades(self):
        l = [9,3,2,1,5,7,2,8,3,4]
        e = 12
        r = max_diff_two_trades(l)
        self.assertEqual(e,r)
        r = max_diff_two_trades_two(l)
        self.assertEqual(e,r)

    def test_swap_array_els(self):
        l = [1,2]
        r = swap_array_els(l, 0, 1)
        self.assertEqual([2,1],r)

    def test_reverse_array_els(self):
        a = [1,2,3,4]
        e = list(reversed(a))
        r = reverse_array_els(a, 0, 3)
        self.assertEqual(r, e)

    def test_reverse_sentence(self):
        s = 'what is your name'
        e = 'name your is what'
        r = reverse_sentence(s)
        self.assertEqual(e,r)

    def test_rotate_array_by(self):
        a = [0,1,2,3,4,5]
        e = [4,5,0,1,2,3]
        r = rotate_array_by(a[:], 2)
        self.assertEqual(e,r)
        r = rotate_array_by(a[:], 8)
        r = self.assertEqual(e,r)

    def test_can_rotate_2d_array(self):
        a = []
        a.append([1,2,3])
        a.append([4,5,6])
        a.append([7,8,9])
        e = [[7,4,1],[8,5,2],[9,6,3]]
        r = rotate_90(a)
        self.assertEqual(e,r)
        m = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        r = rotate_90(m)
        e = [[9, 5, 1, 4], [10, 6, 2, 8], [11, 7, 3, 12]]
        self.assertEqual(r,e)

    def test_it_can_add_two_big_nums(self):
        a = []
        b = [4,8]
        r = add_two_big_nums(a,b)
        self.assertEqual(r, b)
        a = [4,8]
        b = [1,3,3]
        r = add_two_big_nums(a,b)
        self.assertEqual([1,8,1],r)
        a =   [6,4,8]
        b =   [1,3,3]
        e = [7,8,1]
        r = add_two_big_nums(a,b)
        self.assertEqual(e,r)
        a = [9,9]
        b = [9,2]
        e = [1,9,1]
        r = add_two_big_nums(a,b)
        self.assertEqual(e,r)

    def test_it_can_mul_two_big_nums(self):
        a = [1,1]
        b = [3]
        e = [3,3]
        r = mul_two_big_nums(a,b)
        self.assertEqual(e,r)
        a = [1,6,4,3]
        b = [1,3,1]
        e = [2,1,5,2,3,3]
        r = mul_two_big_nums(a,b)
        self.assertEqual(e,r)

    def test_it_can_hash_a_string(self):
        s = 'aaa'
        r = hash_string(s)
        r = hash_string('baa')

    def test_str_str(self):
        s = 'robert'
        t = 'rob'
        r = str_str(s, t)
        self.assertEqual(0, r)
        t = 'ob'

    def test_str_str_three(self):
        s = 'hello world hello'
        t = 'ello'
        r = str_str_three(s, t)
        self.assertEqual([1,13],r)
        t = 'world'
        r = str_str_three(s, t)
        self.assertEqual([6],r)

    def test_str_str_two(self):
        s = 'dogcatdogfishdog'
        n = 'dog'
        r = str_str_two(s, n)
        self.assertEqual([0, 8, 15],r)
    def test_ssearch(self):
        s = 'catdogfish'
        n = 'dog'
        r = ssearch(s, n)
        #print('test_sseoarch',r)

    def test_word_ladder(self):
        word_set = {'hot', 'dot','dog', 'lot','log', 'cog'}
        start = 'hit'
        end = 'cog'
        r = word_ladder(start,end,word_set)
        #print('test_word_ladder 5:',r, r == 5)
        self.assertEqual(5,r)



    def test_word_ladder_two(self):
        word_list = ["hot","dot","dog","lot","log","cog"]
        start = 'hit'
        end = 'cog'
        r = ladder_length(start,end,word_list)
        # s = Solution()
        # r = s.ladderLength(start,end, word_list)
        # print('solution',r)
        self.assertEqual(5,r)

    def test_ww(self):
        word_list = ["hot","dot","dog","lot","log","cog"]
        start = 'hit'
        end = 'cog'
        r = ll(start,end,word_list)
        self.assertEqual(5,r)

    def test_get_set_bits(self):
        # r = get_bit(0,0b100)
        # self.assertEqual(r, 0)
        # r = get_bit(0,0b101)
        # self.assertEqual(r, 1)
        r = get_bit(2,0b101)
        self.assertEqual(r, 1)
        r = get_bit(1,0b0101)
        self.assertEqual(r, 0)
        self.assertEqual(get_bit(3,0b0101), 0)

        r = set_bit(1, 0b0101,1)
        self.assertEqual(r, 7)

        r = set_bit(2, 0b0101,0)
        self.assertEqual(r,1)

    def test_swap_bits(self):
        r = swap_bits(0b0100, 2, 1)
        self.assertEqual(r, 2)
        r = swap_bits(0b010, 2, 1)
        self.assertEqual(0b0100, r)

    def test_reverse_bits(self):
        r = reverse_bits(0b100010)
        r = reverse_bit(0b100010)
        self.assertEqual(r,0b010001)

    def test_count_bits(self):
        r = count_bits(6)
        self.assertEqual(r,2)
        r = count_bits(22)
        self.assertEqual(3,r)

    def test_complement_of_num(self):
        n = '0b00010001'
        r = complement_of_num(int(n, 2))
        self.assertEqual(r, int('0b01110',2))

    def test_primes_sieve(self):
        r = primes_sieve(10)
        self.assertEqual(r, [2,3,5,7])

        r = primes_sieve(101)
        e = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,101]
        self.assertEqual(r,e)

    def test_similar_word_groups(self):
        w = ["star","tars","rats","arts"]
        r = similar_word_groups(w)
        self.assertEqual(2,r)
        w = ["star","tars","rats","arts"]
        r = similar_word_groups_three(w)
        self.assertEqual(2,r)
        w = ["star","tars","rats","arts","frat", "traf", "tarf","carf"]
        r = similar_word_groups_three(w)
        self.assertEqual(r,3)

    def test_chars_exist(self):
        r = base_62_encode(62)
        self.assertEqual(r, 'ba')
        r1 = base_62_decode(r)
        self.assertEqual(62,r1)

    def test_url_coder(self):
        c = UrlCoder()
        for i in range(10):
            c.encode('http://google.com')

        r = c.encode('http://yahoo.com/really/long')

    def test_make_change(self):
        c =  [1,2,5]
        r = make_change(c, 5)
        #print(r)

    def test_k_closest(self):
        K, points = 1, [[1,3],[-2,2],[10,20]]
        r = k_closest_heap(points, K)
        self.assertEqual([(-2, 2)],r)
        r = k_closest_sorted(points, K)
        self.assertEqual([[-2, 2]],r)

    def test_k_smallest(self):
        l = [5,7,4,6,5,3,3]
        l= [5,7,4,6,5,3,3]
        r = select_kth_smallest(l, 3)
        self.assertEqual(4,r)

    def test_kth_largest(self):
        l = [2,1,4,3,5,0]
        r = select_kth_largest(l, 2)
        self.assertEqual(4,r)
        l = [7,2,1,4,3,5,0]
        r = select_kth_largest(l, 3)
        self.assertEqual(4,r)

    def test_it_has_sums_for_k(self):
        l = [2,3,5,6,2,1]
        e = [10,14,13,9]
        k = 3
        r = sliding_window_sum(l,3)
        self.assertEqual(r,e)

    def test_it_calculate_the_max_price_of_a_N_day_period(self):
        l = [[11,1],[19,2],[14,3],[13,4],[4,5],[5,7]]
        e = [13,4]
        r = calculate_the_max_price_of_a_N_day_period(l, 3)
        self.assertEqual(e, r)

    def test_it_sums_two_nums_as_strings(self):
        s1 = "3.14"
        s2 = "0.9"
        e = "4.04"
        r = add_two_big_nums_as_string(s1,s2)
        self.assertEqual(e,r)

        s1 = "3.14"
        s2 = "1.09"
        e = "4.23"
        r = add_two_big_nums_as_string(s1,s2)
        self.assertEqual(e,r)


    def test_zipper(self):
        return
        print('testZipper')
        zipper(2)

if __name__ == '__main__':
    unittest.main()
