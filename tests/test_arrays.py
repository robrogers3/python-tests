import unittest

import arraystuff

class TestArrayStuff(unittest.TestCase):
    def test_reverse(self):
        """
        Test it can revers an array list
        """
        a = [1,2,3]
        r = arraystuff.reverse_list(a)

        self.assertEqual(r, [3,2,1])

    def test_slice_to_target(self):
        """
        test it can slice to target
        """
        a = [1,2,3,5,6,7]
        target = 11
        expect = [5,6]
        r = arraystuff.slice_to_target(a, target)
        a.reverse()
        target = 11
        expect = [1,2]
        r = arraystuff.slice_to_target(a, target)
        self.assertEqual(r, expect)
        a = [2,7,11,15]
        r = arraystuff.slice_to_target(a,33)
        self.assertEqual(r, [1,3])
        a = [3,2,3]
        r = arraystuff.slice_to_target(a,33)
        self.assertEqual(r, [])

    def test_sort_squares_list(self):
        """
        Test it can sort squared list
        """
        a = [-4,-2,-1,0,3,5]
        e = [0,1,4,9,16,25]
        r = arraystuff.sort_squares_list(a)
        self.assertEqual(r, e)

    def test_move_zeros_to_start(self):
        """
        Test we move zeros to start of list
        """
        l = [4,2,0,1,0,3,0]
        e = [0,0,0,1,2,3,4]
        r = arraystuff.move_zeros_to_start(l)
        self.assertEqual(r, e)

    def test_move_zeros_to_end(self):
        """
        Test we move zeros to start of list
        """
        l = [4,2,0,1,0,3,0]
        e = [4,2,3,1,0,0,0]
        r = arraystuff.move_zeros_to_end(l)
        self.assertEqual(r, e)

    def test_partion_using_pivot(self):
        """
        Test we can partiion using pivot
        """
        a = [5,2,4,4,6,4,4,3]
        e = [3,2,4,4,4,4,6,5]
        r = arraystuff.partion_using_pivot(a, 4)
        self.assertEqual(r,e)


    def test_sub_array_equal_to_sum(self):
        a = [1,2,3,5,2]
        e = [3,5]
        r = arraystuff.sub_array_equal_to_sum(a, 8)
        self.assertEqual(r,e)

    def test_max_sum_of_sub_array(self):
        l =  [1,2,-1,2,-3,2,-5]
        e = 4
        r = arraystuff.max_sum_of_sub_array(l)
        self.assertEqual(r,e)

    def test_it_calculate_sliding_windows_sums(self):
        l = [1,4,3,2,5]
        e = [8,9,10]
        r = arraystuff.calculate_sliding_windows_sums(l, 3)
        self.assertEqual(e, r)

    def test_find_n_smallest(self):
        l = [-10,5,3,22,12,1]
        r = arraystuff.find_k_smallest(l, 4)
        self.assertEqual([5,1,3,-10], r)

    def test_find_k_largest(self):
        l = [1,10,3,7,9,2]
        r = arraystuff.find_k_largest(l, 3)
        self.assertEqual(r, [7,10,9])

    def test_it_calculate_the_max_price_of_a_N_day_period(self):
        l = [[11,1],[12,2],[13,3],[4,5],[5,6]]
        e = [13,3]
        r = arraystuff.calculate_the_max_price_of_a_N_day_period(l, 3)
        self.assertEqual(e, r)

    def test_it_can_calculate_max_of_sliding_windows(self):
        l = [4,6,5,2,4,7]
        e = [6,6,5,7]
        r = arraystuff.calculate_max_of_sliding_windows(l, 3)
        self.assertEqual(e,r)


    def test_it_gen_combos_of_list(self):
        l = [1,2,3,4,5]
        r = arraystuff.gen_combos(l, 3)
        e = [[[[1, 2, 3], [1, 2, 4], [1, 2, 5]], [[1, 3, 4], [1, 3, 5]], [[1, 4, 5]]], [[[2, 3, 4], [2, 3, 5]], [[2, 4, 5]]], [[[3, 4, 5]]]]
        self.assertEqual(r,e)

    def test_it_flattens(self):
        l = [[1,2],[[3,4],[[5,6],7]]]
        r = arraystuff.flatten(l, 2)
        self.assertEqual([1, 2, 3, 4, [5, 6], 7],r)

    def test_it_gen_phone_number_words(self):
        num = 24
        r = arraystuff.gen_phone_number_words(num)
        e = [['a', 'g'], ['a', 'h'], ['a', 'i'], ['b', 'g'], ['b', 'h'], ['b', 'i'], ['c', 'g'], ['c', 'h'], ['c', 'i']]
        self.assertEqual(r,e)

    def test_subsets(self):
        l = [1,2,3]
        r = arraystuff.subsets(l)
        e = [[1, 2, 3], [1, 2], [1, 3], 1, [2, 3], 2, 3]
        self.assertEqual(r,e)

    def test_gen_perms(self):
        l = [1,2,3]
        r = arraystuff.gen_perms(l,2)
        e = [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
        self.assertEqual(r,e)


    def test_zig_zag_collect(self):
        m = [[1,2,6],[3,5,7],[4,8,9]]
        r = arraystuff.zig_zag_collect(m)
        e = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(r,e)

    def test_spiral_collect(self):
        m = [[1,2,3],[4,5,6],[7,8,9]]
        # r = arraystuff.spiral_collect(m)
        # e = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        # self.assertEqual(r,e)
        m = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
        r = arraystuff.spiral_collect(m)
        e = [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]

        self.assertEqual(r,e)

    def test_rotate_ninty(self):
        a = []
        a.append([1,2,3])
        a.append([4,5,6])
        a.append([7,8,9])
        e = [[7,4,1],
             [8,5,2],
             [9,6,3]]
        r = arraystuff.rotate_ninty(a)
        self.assertEqual(e,r)
        m = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
        r = arraystuff.rotate_ninty(m)


    def test_transpose(self):
        a = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        r = arraystuff.transpose(a)

    def test_rotate_90_clockwise(self):
        a = [
            [1,2,3],
            [4,5,6],
            [7,8,9],
            ]

        e = [
            [7,4,1],
            [8,5,2],
            [9,6,3]
            ]
        r = arraystuff.rotate_ninty_clockwise(a)
        #self.assertEqual(a,e)

    def test_transpose(self):
        a = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        r = arraystuff.transpose(a)
        e = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertEqual(e,r)

    def test_rotate_minus_90(self):
        a = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        r = arraystuff.transpose(a)
        r1 = arraystuff.reverse_columns(r)
        e = [[7,4,1],
             [8,5,2],
             [9,6,3]]

    def test_reverse_columns(self):
        a = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        r = arraystuff.reverse_columns(a)

    def test_reverse_array(self):
        a = [1,2,3]
        r = arraystuff.reverse_array(a)
        self.assertEqual([3,2,1],a)

    def test_find_missing_num(self):
        a = [1,2,3,5]
        self.assertEqual(4,arraystuff.find_missing_num(a,5))
        self.assertEqual(2,arraystuff.find_missing_num([1,3,4,5],5))

    def test_find_single_number(self):
        a = [11,12,11,12,15,15,7]
        self.assertEqual(7, arraystuff.find_single_number(a))

    def test_k_smallest(self):
        l= [5,7,4,6,5,3,3]
        r = arraystuff.select_kth_smallest(l, 3)
        self.assertEqual(4,r)
        l= [3,7,4,6,5,3,3]
        r = arraystuff.select_kth_smallest(l, 4)
        self.assertEqual(4,r)

    def test_kth_largest(self):
        l = [2,1,4,3,5,0]
        r = arraystuff.select_kth_largest(l, 2)
        self.assertEqual(4,r)
        l = [7,2,1,4,3,5,0]
        r = arraystuff.select_kth_largest(l, 3)
        self.assertEqual(4,r)

    def test_merge_sort(self):
        l = [2,5,1,10,4,3]
        e = [1,2,3,4,5,10]
        l = arraystuff.merge_sort(l)
        self.assertEqual(e,l)

    def test_merge_sort(self):
        l = [2,5,1,10,4,3]
        e = [1,2,3,4,5,10]
        r = arraystuff.quick_sort(l)
        self.assertEqual(e,r)
        s = """ccc
        aaa
        ttt""";

        lines = [l.strip() for l in s.split("\n") if l]
        r = arraystuff.quick_sort(lines)
        self.assertEqual(['aaa', 'ccc', 'ttt'], r)


    def test_bucket_sort(self):
        l = [2,5,0,1,6,4,3]
        e = [0,1,2,3,4,5,6]
        r = arraystuff.bucket_sort(l)
        self.assertEqual(r,e)

    def test_sort_lists(self):
        m = [ [1, 3, 5, 7],
              [2, 4, 6, 8],
              [0, 9, 10, 11]]
        e = list(map(int, "0 1 2 3 4 5 6 7 8 9 10 11".split(" ")))
        r = arraystuff.sort_lists(m)
        self.assertEqual(r,e)

    def test_length(self):
        l = [2,5,0,1,6,4,3]
        r = arraystuff.length(l)
        self.assertEqual(r,len(l))

    def test_dnf(self):
        a = [1,2,3,4,4,1,2,3]
        i = 2
        e = [1,2,2,1,3,3,4,4]
        r = arraystuff.dnf(a,i)
        self.assertEqual(r, e)

if __name__ == '__main__':
    unittest.main()
